from flask import Blueprint, request, jsonify
from App.models import *
from App.blueprints.format import *
import uuid

bp = Blueprint("data_products", __name__, url_prefix='/dp')

@bp.route('', methods = ['GET'])
def total():
    owner_id = request.args.get('owner_id')
    page = int(request.args.get('page'))
    per_page = 15

    data_products = DataProductsModel.query.filter_by(owner_id = owner_id).offset((page-1)*per_page).limit(per_page)
    return res_format(200,to_list(data_products),'查询成功！')

@bp.route('/count', methods = ['GET'])
def count():
    owner_id = request.args.get('owner_id')
    data = DataProductsModel.query.filter_by(owner_id=owner_id).all()
    return res_format(200, len(data), '查询成功')

@bp.route('/img',methods = ['POST'])
def upload_img():
    img = request.files.get('file')
    filesFormat = img.filename.split('.')[-1]
    path = 'App/static/data_products/img/{}.{}'.format(uuid.uuid4(),filesFormat)
    img.save('App/static' + path)
    return res_format(200, path, '上传成功')

@bp.route('/create',methods = ['POST'])
def create():
    data_product = DataProductsModel()
    data_product.name = request.form.get('name')
    data_product.audit_status = request.form.get('audit_status')
    data_product.nominal_price = request.form.get('nominal_price')
    data_product.pre_img = request.form.get('pre_img')
    data_product.products_description = request.form.get('products_description')
    data_product.application_scenario = request.form.get('application_scenario')
    data_product.data_asset_id = request.form.get('data_asset_id')
    data_product.owner_id = request.form.get('owner_id')
    data_product.property_range = request.form.get('property_range')
    data_product.time_limit = request.form.get("time_limit").replace('T', '\t').replace('.000Z', '')
    data_product.market_status = '未上架'

    db.session.add(data_product)
    db.session.commit()

    return res_format(200,[],'success!')

@bp.route('/renew',methods = ['POST'])
def renew():
    id  = request.form.get('id')
    data_product = DataProductsModel.query.get(id)
    data_product.name = request.form.get('name')
    data_product.audit_status = request.form.get('audit_status')
    data_product.nominal_price = request.form.get('nominal_price')
    data_product.pre_img = request.form.get('pre_img')
    data_product.products_description = request.form.get('products_description')
    data_product.application_scenario = request.form.get('application_scenario')
    data_product.data_asset_id = request.form.get('data_asset_id')
    data_product.market_status = '未上架'
    data_product.audit_status = '已提交审核'

    db.session.commit()
    return res_format(200, [], '上传成功')

@bp.route('/renew_market_status',methods = ['POST'])
def update_market_status():
    id  = request.form.get('id')
    print(id)
    market_status = request.form.get('market_status')
    # audit_status = request.form.get('audit_status')
    data_product = DataProductsModel.query.get(id)
    data_product.market_status = market_status
    db.session.commit()
    return res_format(200, [], '商品状态更新成功')

@bp.route('/countPass', methods = ['GET'])
def countPass():
    # owner_id = request.args.get('owner_id')
    data = DataProductsModel.query.filter_by(market_status = '已上架').all()
    return res_format(200, len(data), '查询成功')

@bp.route('/getPass', methods = ['GET'])
def getPass():
    page = int(request.args.get('page'))
    per_page = 6
    res = []
    data_products = DataProductsModel.query.filter_by(market_status = '已上架').offset((page - 1) * per_page).limit(per_page)
    for item in data_products:
        da = DataAssetModel.query.get(item.data_asset_id)
        da_json = {
            'industry_division': da.industry_division,
            'data': da.data,
            'keyword': da.keyword,
            'type': da.type
        }
        seller = AccountModel.query.get(item.owner_id)
        seller_json = {
            "seller_name" : seller.name
        }
        res.append(merge_dict(item.to_json(),da_json,seller_json))

    return res_format(200, res, '查询成功')


@bp.route('/getProductsAudit',methods = ['GET'])
def getProductsAudit():
    page = int(request.args.get('page'))
    per_page = 15
    qc = DataProductsModel.query.filter_by(audit_status = '已提交审核').offset((page-1)*per_page).limit(per_page)
    return res_format(200,to_list(qc),'查询成功')

@bp.route('/renewProductsAudit',methods = ['POST'])
def renewProductsAuit():
    id = request.form.get('id')
    audit_status = request.form.get('audit_status')
    asset = DataProductsModel.query.get(id)
    asset.audit_status = audit_status

    db.session.commit()

    return res_format(200, [], '审核结果已提交！')

@bp.route('/getProductsAuditCount',methods = ['GET'])
def getProductsAuditCount():
    data = DataProductsModel.query.filter_by(audit_status = '已提交审核').all()
    return res_format(200, len(data), '查询成功')