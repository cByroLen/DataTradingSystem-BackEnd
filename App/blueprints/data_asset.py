from flask import Blueprint, request, jsonify
from App.models import *
from App.blueprints.format import *
import uuid

Gobal_path = 'E:/Programming/python_projec/DataTradingSystem_Flask/'
bp = Blueprint("data_asset", __name__, url_prefix='/da')


@bp.route('', methods = ['GET'])
def total():
    owner_id = request.args.get('owner_id')
    page = int(request.args.get('page'))
    per_page = 15

    data_asset = DataAssetModel.query.filter_by(owner_id = owner_id).offset((page-1)*per_page).limit(per_page)
    return res_format(200,to_list(data_asset),'查询成功')

@bp.route('/count', methods = ['GET'])
def count():
    owner_id = request.args.get('owner_id')
    data = DataAssetModel.query.filter_by(owner_id = owner_id).all()
    return res_format(200,len(data),'查询成功')

@bp.route('/getPass', methods = ['GET'])
def getPass():
    owner_id = request.args.get('owner_id')
    data = DataAssetModel.query.filter_by(owner_id = owner_id, audit_status = '审核已通过').all()
    return res_format(200,to_list(data),'查询成功')

@bp.route('/renew',methods = ['POST'])
def renew_data():
    id = request.form.get('id')
    asset = DataAssetModel.query.get(id)


    asset.name = request.form.get('name')
    asset.keyword = request.form.get('keyword')
    asset.industry_division = request.form.get('industry_division')
    asset.type = request.form.get("type")
    asset.property_range = request.form.get("property_range")
    asset.size = request.form.get("size")
    asset.data = request.form.get("data")
    asset.traceability_certification_documents = request.form.get("traceability_certification_documents")
    asset.quality_assessment_report = request.form.get("quality_assessment_report")
    asset.audit_status = request.form.get("audit_status")
    asset.format = request.form.get("format")
    asset.begin_time = request.form.get("begin_time").replace('T','\t').replace('.000Z','')
    asset.renew_time = request.form.get("renew_time").replace('T','\t').replace('.000Z','')
    asset.audit_status = '已提交审核'
    db.session.commit()
    return res_format(200,[],'上传成功')

@bp.route('/data',methods = ['POST'])
def upload_data():
    data_file = request.files.get('file')
    filesFormat = data_file.filename.split('.')[-1]
    path = '/data_asset/data/{}.{}'.format(uuid.uuid4(),filesFormat)
    data_file.save('App/static' + path)
    return res_format(200,path,'上传成功')


@bp.route('/TCD',methods = ['POST'])
def upload_TCD():
    tcd_file = request.files.get('file')
    filesFormat = tcd_file.filename.split('.')[-1]
    path = '/data_asset/tcd/{}.{}'.format(uuid.uuid4(),filesFormat)
    tcd_file.save('App/static' + path)
    return res_format(200, path, '上传成功')

@bp.route('/QAR',methods = ['POST'])
def upload_QAR():
    qar_file = request.files.get('file')
    filesFormat = qar_file.filename.split('.')[-1]
    path = '/data_asset/qar/{}.{}'.format(uuid.uuid4(),filesFormat)
    qar_file.save('App/static' + path)
    return res_format(200,path, '上传成功')

@bp.route('/create',methods = ['POST'])
def create():
    data_asset = DataAssetModel()
    data_asset.name = request.form.get('name')
    data_asset.keyword = request.form.get('keyword')
    data_asset.industry_division = request.form.get('industry_division')
    data_asset.type = request.form.get('type')
    data_asset.property_range = request.form.get('property_range')
    data_asset.size = request.form.get('size')
    data_asset.data = request.form.get('data')
    data_asset.traceability_certification_documents = request.form.get('traceability_certification_documents')
    data_asset.quality_assessment_report = request.form.get('quality_assessment_report')
    data_asset.audit_status = request.form.get('audit_status')
    data_asset.format = request.form.get('format')
    data_asset.begin_time = request.form.get('begin_time').replace('T','\t').replace('.000Z','')
    data_asset.renew_time = request.form.get('renew_time').replace('T','\t').replace('.000Z', '')
    data_asset.owner_id = int(request.form.get('owner_id'))

    print(data_asset.begin_time)
    db.session.add(data_asset)
    db.session.commit()

    return res_format(200,[],'success!')

@bp.route('/getAssetAudit',methods = ['GET'])
def getAssetAudit():
    page = int(request.args.get('page'))
    per_page = 15
    qc = DataAssetModel.query.filter_by(audit_status = '已提交审核').offset((page-1)*per_page).limit(per_page)
    return res_format(200,to_list(qc),'查询成功')

@bp.route('/renewAssetAudit',methods = ['POST'])
def renewAssetAuit():
    id = request.form.get('id')
    audit_status = request.form.get('audit_status')
    asset = DataAssetModel.query.get(id)
    asset.audit_status = audit_status

    db.session.commit()

    return res_format(200, [], '审核结果已提交！')

@bp.route('/getAssetAuditCount',methods = ['GET'])
def getAssetAuditCount():
    data = DataAssetModel.query.filter_by(audit_status = '已提交审核').all()
    return res_format(200, len(data), '查询成功')
