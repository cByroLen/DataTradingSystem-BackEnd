from App.models import *
from App.blueprints.format import *

bp = Blueprint("tranction_contract", __name__, url_prefix='/tc')

@bp.route('', methods = ['GET'])
def total():
    buyer_id = request.args.get('buyer_id')
    tc = TransactionContractModel.query.filter_by(buyer_id = buyer_id,effective_or_not = '是').all()
    res = []
    for item in tc:
        dp = DataProductsModel.query.get(item.data_products_id)
        dp_json = {
            'products_description' : dp.products_description,
            'property_range':dp.property_range,
            'application_scenario':dp.application_scenario,
            'time_limit':dp.time_limit,
            'name':dp.name,
            'nominal_price':dp.nominal_price
        }
        da = DataAssetModel.query.get(dp.data_asset_id)
        da_json = {
            'industry_division' : da.industry_division,
            'data': da.data,
            'keyword':da.keyword,
            'type':da.type
        }
        buyer = AccountModel.query.get(item.buyer_id)
        buyer_json = {
            'buyer_name' : buyer.name
        }
        seller = AccountModel.query.get(item.seller_id)
        seller_json = {
            'seller_name': seller.name
        }

        c = merge_dict(item.to_json(),dp_json,da_json,buyer_json,seller_json)
        res.append(c)

    return res_format(200,res,'查询成功')

@bp.route('/count', methods = ['GET'])
def count():
    buyer_id = request.args.get('buyer_id')
    data = TransactionContractModel.query.filter_by(buyer_id=buyer_id).all()
    return res_format(200, len(data), '查询成功')

@bp.route('/create',methods = ['POST'])
def create():
    tc = TransactionContractModel()
    tc.data_products_id = request.form.get('data_products_id')
    tc.buyer_id = request.form.get('buyer_id')
    tc.seller_id = request.form.get('seller_id')
    tc.tradding_time = datetime.now()
    tc.effective_or_not = '是'

    db.session.add(tc)
    db.session.commit()
    return res_format(200, [], '交易成功')