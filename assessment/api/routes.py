from flask import Blueprint, request, jsonify
from assessment.models import Doctor, Appointment, appt_schema, appts_schema, docs_schema, db

api = Blueprint('api', __name__, url_prefix='/api')

#Helpers 
def time_validator(time):
    return time[-2:] in ['00', '15', '30', '45']

def kind_validator(kind):
    return kind == 'Follow-Up' or kind == 'New Patient'


# GET all docs
@api.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = Doctor.query.all()
    res = docs_schema.dump(doctors)
    return jsonify(res)

# GET all appointments for particular doctor on particular day
@api.route('doctors/<doctor_id>/<day>', methods=['GET'])
def get_appt_by_doctor(doctor_id, day):
    appointments = Appointment.query.filter_by(doctor_id = doctor_id).all()
    filtered_appointments = filter(lambda x: x.date.startswith(day.replace('-','/',)), appointments)
    response = appts_schema.dump(filtered_appointments)
    return jsonify(response)


# CREATE a new appointment
@api.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.json
    doctor_id = data['doctor_id']
    date = data['date']
    time = date.split(' ')[1]
    kind = data['kind']
    # check to see that doctor ID is valid
    doctor = Doctor.query.filter_by(id = doctor_id).first()
    if not doctor:
        return {"Error": "Doctor ID not found"}, 404
    # check to see if time is valid:
    if not time_validator(time):
        return {"Error":"Please enter a valid time"}, 409
    if not kind_validator(kind):
        return {"Error":"Please enter a valid appointment kind"}, 409
    # query the doctor's current appointments of that time
    same_time_appointments = Appointment.query.filter_by(date = date).all()
    if len(same_time_appointments) == 3:
        return {"Error": "Already 3 appointments scheduled"}, 409
    
    appt = Appointment(data['first_name'], data['last_name'], data['kind'], 
    data['date'], data['time'], data['doctor_id'])
    db.session.add(appt)
    db.session.commit()
    response = appt_schema.dump(appt)
    return jsonify(response)


# DELETE Appointment
@api.route('/appointments/<id>', methods=['DELETE'])
def delete_appt(id):
    appt = Appointment.query.get(id)
    if appt:
        db.session.delete(appt)
        db.session.commit()
        return jsonify({'Success': f'Appt ID #{appt.id} has been deleted'}), 300
    return jsonify({'Error': 'That appt ID does not exist!'}), 404






@api.route('/appointments/<id>', methods=['PATCH'])
# @admin_required
def update_appt(id):
    appt = Appointment.query.get(id)
    date_time = request.json['time']
    time = date_time.split(' ')[1]
    print(time)
    if appt:
        if not time_validator(time):
            return {"Error":"Please enter a valid time"}, 409
        appt.time = time
        db.session.add(appt)
        db.session.commit()
        response = appt_schema.dump(appt)
        return jsonify(response)
    return {"Error": "Appointment not found"}, 404
        