from flask import Blueprint, request ,jsonify
from App.models import *
from App.blueprints.format import *
import uuid

bp = Blueprint("user", __name__, url_prefix='/user')
# 登录
@bp.route('/login', methods = ['POST'])
def login():
    phone = str(request.form.get('phone'))
    password =request.form.get('password')
    account = AccountModel.query.filter_by(phone = phone)

    if account.first() == None:
        return res_format(201,[],'用户不存在!')
    if account.first().password != password:
        return res_format(202,[],'用户名或密码错误！')

    cookies = {
        "id":account.first().id,
        "name":account.first().name,
        "authority":account.first().authority,
    }

    return res_format(200,cookies,'登陆成功！')

@bp.route('/reg', methods = ['POST'])
def reg():
    account = AccountModel()
    account.name = request.form.get('id')
    account.password = request.form.get('password')
    account.phone = request.form.get('phone')
    account.email = request.form.get('email')
    account.authority = '未认证用户'

    print(account.phone)
    print(AccountModel.query.filter_by(phone = account.phone).first())

    if AccountModel.query.filter_by(phone = account.phone).first() != None:
        return res_format(201,[],'该手机已注册！')
    if AccountModel.query.filter_by(email = account.email).first() != None :
        return res_format(202,[],"该邮箱已注册！")

    db.session.add(account)
    db.session.commit()

    return res_format(200,[],'注册成功！')

@bp.route('/qc/CL',methods = ['POST'])
def upload_CL():
    CompanyLicense = request.files.get('file')
    filesFormat = CompanyLicense.filename.split('.')[-1]
    path = 'App/static/user/company_license/{}.{}'.format(uuid.uuid4(),filesFormat)
    CompanyLicense.save('App/static' + path)
    return res_format(200, path, '上传成功')

@bp.route('/qc/BI',methods = ['POST'])
def upload_BI():
    BankInfo = request.files.get('file')
    filesFormat = BankInfo.filename.split('.')[-1]
    path = 'App/static/user/bank_info/{}.{}'.format(uuid.uuid4(),filesFormat)
    BankInfo.save('App/static' + path)
    return res_format(200, path, '上传成功')

@bp.route('/qc',methods = ['POST','GET'])
def qc():
    if request.method == 'POST':
        qc = UserQCModel()
        qc.c_unified_social_credit_code = request.form.get('c_unified_social_credit_code')
        qc.c_name = request.form.get('c_name')
        qc.c_type = request.form.get('c_type')
        qc.c_scrope = request.form.get('c_scrope')
        qc.c_license_type = request.form.get('c_license_type')
        qc.c_license = request.form.get('c_license')
        qc.m_name = request.form.get('m_name')
        qc.m_phone = request.form.get('m_phone')
        qc.m_license_type = request.form.get('m_license_type')
        qc.m_license = request.form.get('m_license')
        qc.b_account_info = request.form.get('b_account_info')
        qc.b_bank = request.form.get('b_bank')
        qc.b_institution = request.form.get('b_institution')
        qc.b_account = request.form.get('b_account')
        qc.b_account_name = request.form.get('b_account_name')
        qc.l_name = request.form.get('l_name')
        qc.l_area = request.form.get('l_area')
        qc.l_address = request.form.get('l_address')
        qc.l_code = request.form.get('l_code')
        qc.l_email = request.form.get('l_email')
        qc.l_website = request.form.get('l_website')
        qc.l_phone = request.form.get('l_phone')
        qc.account_id = request.form.get('account_id')
        qc.audit_status = '已提交审核'

        db.session.add(qc)
        db.session.commit()
        return res_format(200,[],'success')

    else:
        pass


@bp.route('/getQcAudit',methods = ['GET'])
def qcAudit():
    page = int(request.args.get('page'))
    per_page = 15
    qc = UserQCModel.query.filter_by(audit_status = '已提交审核').offset((page-1)*per_page).limit(per_page)


    return res_format(200,to_list(qc),'查询成功')

@bp.route('/renewQcAudit',methods = ['POST'])
def renewQcAuit():
    id = request.form.get('id')
    audit_status = request.form.get('audit_status')
    qc = UserQCModel.query.get(id)
    qc.audit_status =  audit_status
    account = AccountModel.query.get(qc.account_id)
    account.authority = '已认证用户'

    db.session.commit()

    return res_format(200,[],'审核结果已提交')

@bp.route('/getQcAuditCount',methods = ['GET'])
def getQcAuditCount():
    data = UserQCModel.query.filter_by(audit_status = '已提交审核').all()
    return res_format(200, len(data), '查询成功')











