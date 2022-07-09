# import json

from flask import Flask

from main1 import search_verbs_synonym

app = Flask(__name__)

CATEGORY =  {   
    "payment": {
        "electricity": {
                        "description": "Thanh toán hoá đơn điện",
                        "id": "urn:directory:app:83304571677442071",
                        "identifier": "83304571677442071",
                        "image_url": "https://salt.tikicdn.com/ts/miniapp/7c/d3/5d/d6d81bde2b8da3d4d7d691539884b19a.png",
                        "metadata": {
                            "badge": "",
                            "deep_link": "tikivn://billpay/1",
                            "kind": "tikiapp"
                        },
                            "name": "Điện",
                            "total_unique_user": 0,
                            "total_used": 32158
                        }
,
        "water": {
                    "description": "Thanh toán hoá đơn nước",
                    "id": "urn:directory:app:83301987348643851",
                    "identifier": "83301987348643851",
                    "image_url": "https://salt.tikicdn.com/ts/miniapp/63/5f/ca/28a5f795f32641010c78c7f77ab1496e.png",
                    "metadata": {
                        "badge": "",
                        "deep_link": "tikivn://billpay/2",
                        "kind": "tikiapp"
                    },
                    "name": "Nước",
                    "total_unique_user": 0,
                    "total_used": 9092
                },
        "loan": {
                    "description": "Thanh toán hoá đơn vay tiêu dùng",
                    "id": "urn:directory:app:83305032413347847",
                    "identifier": "83305032413347847",
                    "image_url": "https://salt.tikicdn.com/ts/miniapp/2c/94/81/b2a77910963ba47dd874dc58eddd14d3.png",
                    "metadata": {
                        "badge": "MỚI",
                        "deep_link": "tikivn://billpay/13",
                        "kind": "tikiapp"
                    },
                    "name": "Vay tiêu dùng",
                    "total_unique_user": 0,
                    "total_used": 12563
                },
        "phone card": {
                        "description": "Nạp tiền điện thoại nhanh trên Tiki",
                        "id": "urn:directory:app:83306411265622025",
                        "identifier": "83306411265622025",
                        "image_url": "https://salt.tikicdn.com/ts/miniapp/56/be/da/8da52249e33d271633abe91537adf982.png",
                        "metadata": {
                            "badge": "",
                            "deep_link": "tikivn://webview?url=https://tiki.vn/san-pham-so/nap-tien-dien-thoai-tra-truoc?src=top_app_icon",
                            "kind": "tikiapp"
                        },
                        "name": "Nạp tiền điện thoại",
                        "total_unique_user": 0,
                        "total_used": 10939
                    },
        "phone data": {
                        "description": "Mua mã thẻ data 3G/4G trên Tiki",
                        "id": "urn:directory:app:83306036261290007",
                        "identifier": "83306036261290007",
                        "image_url": "https://salt.tikicdn.com/ts/miniapp/7a/66/8a/a69a341f735c11006e795b4c55d4a2a0.png",
                        "metadata": {
                            "badge": "",
                            "deep_link": "tikivn://webview?url=https://tiki.vn/san-pham-so/the-cao-data?src=top_app_icon",
                            "kind": "tikiapp"
                        },
                        "name": "Mã thẻ data 3G/4G",
                        "total_unique_user": 0,
                        "total_used": 956
                    }

    },
    "finance": {
        "investment": {
                        "description": "Đầu tư và tích lũy một cách dễ dàng, tiện lợi",
                        "id": "urn:directory:app:87318023127433247",
                        "identifier": "vn.infina.tikiapp",
                        "image_url": "https://salt.tikicdn.com/ts/miniapp/3d/00/07/a4385accd2d5de726d6f7b90be1328af.png",
                        "metadata": {
                            "badge": "",
                            "kind": "tiniapp"
                        },
                        "name": "Infina - Đầu tư & Tích lũy",
                        "total_unique_user": 46740,
                        "total_used": 8466
                    },
        "trade": {
                    "description": "Tiki Exchange là một sàn giao dịch được Tiki lập ra giúp việc trao đổi giữa Astra và Tiki Xu 1 cách dễ dàng. Khách hàng của Tiki có sở hữu Astra sẽ được phép thực hiện việc trao đổi Astra của mình cho khách hàng khác của Tiki tại Tiki App",
                    "id": "urn:directory:app:117514104318459933",
                    "identifier": "vn.tiki.miniapp.tikiexchange",
                    "image_url": "https://salt.tikicdn.com/ts/miniapp/e1/d8/2a/7a79703396f2653909b9c01df7bcd893.png",
                    "metadata": {
                        "badge": "MỚI",
                        "kind": "tiniapp"
                    },
                    "name": "Tiki Exchange",
                    "total_unique_user": 304827,
                    "total_used": 4729
                },
        "loan": {
                    "description": "Vclick là Chợ Tín dụng minh bạch giúp bạn tìm khoản vay có điều kiện tốt nhất từ các ngân hàng và công ty tài chính. Áp dụng công nghệ 4.0, VClick phối hợp cùng các đối tác cung cấp dịch vụ vay với thủ tục đơn giản, không cần gặp mặt và thời gian phê duyệt giải ngân nhanh nhất.",
                    "id": "urn:directory:app:144994304950075400",
                    "identifier": "vn.tiki.miniapp.vclick",
                    "image_url": "https://salt.tikicdn.com/ts/miniapp/55/7d/a3/d2550f69cde5fb8bac85020519cb4be4.png",
                    "metadata": {
                        "badge": "",
                        "kind": "tiniapp"
                    },
                    "name": "Đăng ký vay VClick",
                    "total_unique_user": 1508,
                    "total_used": 2478
                }

    },
    "food": {
        "food": {
                    "description": "Thèm giao đồ ăn nhanh nhất trên Tiki. Các món ăn, nhà hàng và thực phẩm yêu thích của bạn đã được Thèm chọn lọc và sắp xếp theo từng bộ sưu tập món một cách cá nhân hóa nhất. Hãy để chúng mình xua tan cơn đói của bạn và cảm nhận được cảm giác Thèm đúng chuẩn!",
                    "id": "urn:directory:app:134273842183995422",
                    "identifier": "app.ketnoi.miniapp.them",
                    "image_url": "https://salt.tikicdn.com/ts/miniapp/f0/eb/97/0a36ffe52044be633341ff5193124b2b.png",
                    "metadata": {
                        "badge": "",
                        "kind": "tiniapp"
                    },
                    "name": "Thèm - Đặt đồ ăn",
                    "total_unique_user": 16320,
                    "total_used": 2828
                }

    },
    "shopping": {
        "clothes": {
                    "description": "Coolmate là giải pháp mua sắm online cả tủ đồ cho nam giới gồm đầy đủ áo thun, quần short, quần lót, tất(vớ), phụ kiện, đồ thể thao. Coolmate cung cấp chính sách 100% khách hàng hài lòng, đổi trả không hỏi lý do trong vòng 60 ngày với chất lượng tốt và giá cả cạnh tranh",
                    "id": "urn:directory:app:140716007697219596",
                    "identifier": "vn.miniapp.coolmate",
                    "image_url": "https://salt.tikicdn.com/ts/miniapp/cf/b4/7a/f2cd4eb2d1a68a87be0fbc723fb6cd28.png",
                    "metadata": {
                        "badge": "",
                        "kind": "tiniapp"
                    },
                    "name": "Thời trang Coolmate",
                    "total_unique_user": 19912,
                    "total_used": 5300
                },
        "beauty": {
                        "description": "BeautyX giúp người dùng tìm kiếm và mua dịch vụ online.\nMột số tính năng nổi bật mà beautyX cung cấp:\n- Đặt lịch làm đẹp online.\n- Quản lý lịch hẹn.\n- Tìm kiếm spa, thẩm mỹ việc, tiệm nails, ... gần bạn.\n- Mua dịch vụ, sản phẩm, liệu trình và thanh toán online.",
                        "id": "urn:directory:app:175029957787975701",
                        "identifier": "vn.myspa.beautyx",
                        "image_url": "https://salt.tikicdn.com/ts/miniapp/40/5e/0b/c34cf75b3e7e91dd0a76dbf01998b058.png",
                        "metadata": {
                            "badge": "-50%",
                            "kind": "tiniapp"
                        },
                        "name": "BeautyX",
                        "total_unique_user": 302,
                        "total_used": 611
                    },

        "gas": {
                    "description": "Đặt gas, nước và hàng tiêu dùng nhanh chóng. \nMiễn phí giao hàng, giao Gas chỉ 15 phút kèm nhiều quà tặng hấp dẫn. Nước 1 bình cũng giao nhanh chóng. Hàng tiêu dùng đầy đủ phục vụ nhu cầu. \nTổng đài đặt hàng 1900 1565.",
                    "id": "urn:directory:app:165334619678310402",
                    "identifier": "gas.dung.com.gas24h",
                    "image_url": "https://salt.tikicdn.com/ts/miniapp/08/70/1e/3d07db89242ba9e69bcd772829daac95.png",
                    "metadata": {
                        "badge": "GIẢM 500k",
                        "kind": "tiniapp"
                    },
                    "name": "Gas24h",
                    "total_unique_user": 289,
                    "total_used": 729
                }

    },
    "medical": {
        "medicine": {
                        "description": "Tư vấn, giao dược phẩm trong 20 phút, phục vụ 24H",
                        "id": "urn:directory:app:127921481869950982",
                        "identifier": "com.medigo.miniapp.user",
                        "image_url": "https://salt.tikicdn.com/ts/miniapp/44/b3/d9/b6a9e3f278c459eedeb283276e380584.png",
                        "metadata": {
                            "badge": "FREESHIP",
                            "kind": "tiniapp"
                        },
                        "name": "Đặt Thuốc Medigo",
                        "total_unique_user": 19484,
                        "total_used": 2971
                    }

    },
    "insurance": {
        "travel insurance": {
                                "description": "Mua ngay bảo hiểm du lịch Liberty trên Tiki",
                                "id": "urn:directory:app:83305465970163718",
                                "identifier": "83305465970163718",
                                "image_url": "https://salt.tikicdn.com/ts/miniapp/11/ba/1c/11e3ac5668f20692e69058435c8deb58.png",
                                "metadata": {
                                    "badge": "",
                                    "deep_link": "tikivn://webview?url=https://tiki.vn/liberty?src=top_app_icon",
                                    "kind": "tikiapp"
                                },
                                "name": "BH du lịch Liberty",
                                "total_unique_user": 0,
                                "total_used": 378
                            },
        "car insurance": {
                            "description": "Bảo vệ tức thì, chỉ từ 65k. Khám phá ngay!",
                            "id": "urn:directory:app:164554316412092433",
                            "identifier": "164554316412092433",
                            "image_url": "https://salt.tikicdn.com/ts/miniapp/bc/a4/d8/12934334b208329e67dfdb1625543e0d.png",
                            "metadata": {
                                "badge": "MỚI",
                                "deep_link": "tikivn://insurance-tech/pdp?id=62",
                                "kind": "tikiapp"
                            },
                            "name": "Bảo hiểm ô tô",
                            "total_unique_user": 0,
                            "total_used": 245
                        },
        "bike insurance": {
                            "description": "Chỉ từ 1K, an toàn mọi nẻo đường. Bảo vệ ngay!",
                            "id": "urn:directory:app:115738259811729421",
                            "identifier": "115738259811729421",
                            "image_url": "https://salt.tikicdn.com/ts/miniapp/90/4c/19/621f126027ded8c03edf1c21edd4485f.png",
                            "metadata": {
                                "badge": "",
                                "deep_link": "tikivn://insurance-tech/pdp?id=76",
                                "kind": "tikiapp"
                            },
                            "name": "Bảo hiểm xe máy",
                            "total_unique_user": 0,
                            "total_used": 963
                        }

    },
    "entertainment": {
        "movie tickets": {
                            "description": "Mua vé xem phim & sự kiện hot tại Ticketbox",
                            "id": "urn:directory:app:83313446371721217",
                            "identifier": "83313446371721217",
                            "image_url": "https://salt.tikicdn.com/ts/miniapp/46/5d/92/d6aa6dd030e28677548b53c7b4ab92b2.png",
                            "metadata": {
                                "badge": "",
                                "deep_link": "tikivn://webview?url=https://tiki.vn/ticketbox?src=top_app_icon",
                                "kind": "tikiapp"
                            },
                            "name": "Ticketbox",
                            "total_unique_user": 0
                            

                            }
                    },
    "travel": {
        "plane ticket": {
                            "description": "Đặt vé máy bay giá rẻ hơn tại Tiki",
                            "id": "urn:directory:app:83305789384556559",
                            "identifier": "83305789384556559",
                            "image_url": "https://salt.tikicdn.com/ts/miniapp/66/17/50/22402e7d46e3cb8a083d5244a19abdd7.png",
                            "metadata": {
                                "badge": "ƯU ĐÃI",
                                "deep_link": "tikivn://webview?url=https%3A%2F%2Ftiki.vn%2Fdat-ve-may-bay",
                                "kind": "tikiapp"
                            },
                            "name": "Vé máy bay",
                            "total_unique_user": 0,
                            "total_used": 4502
                        },
        "bus ticket": {
                        "description": "Đặt vé xe khách tiện lợi trên Tiki",
                        "id": "urn:directory:app:83305877381054480",
                        "identifier": "83305877381054480",
                        "image_url": "https://salt.tikicdn.com/ts/miniapp/9c/0c/34/1b29336421a4be64289c600814dd0206.png",
                        "metadata": {
                            "badge": "GIẢM 8%",
                            "deep_link": "tikivn://webview?url=https://tiki.vn/san-pham-so/ve-xe-khach?src=top_app_icon",
                            "kind": "tikiapp"
                        },
                        "name": "Vé xe khách",
                        "total_unique_user": 0,
                        "total_used": 1549
                    }
        
    }
}

@app.route('/category/<string:querry>/', methods=['GET'])
def get_users(querry):
    

    # syns = search_synonym(querry)
    # list_syn = syns[0]["synonyms"]

    # keys = CATEGORY.keys()
    # result  = {}
    # for syn in list_syn:
    #     if syn in keys:
    #         result[syn] = CATEGORY[syn]
    #         break
    # return result
    
    result = search_verbs_synonym(querry)

    if "verb" not in result[0]:
        re_querry = search_verbs_synonym("tôi " + querry)
        used_result = re_querry[0]
    else:
        used_result = result[0]

    print(f'used result: {used_result}')
    possible_category = {}
    for key, value in CATEGORY.items():
       
        if 'verb' in used_result and key in used_result['verb']:
            possible_category["key"] = key
        elif 'noun' in used_result:
            for noun in used_result['noun']:
                if possible_category:
                    break
                else:
                    for value in CATEGORY.values():
                        if noun in value and noun not in possible_category:
                            
                            possible_category["value"] = noun
                        
                # print(nn)
                # if noun in CATEGORY.values():

    print(f'poss cate: {possible_category}')    

    if "key" in possible_category:
        return CATEGORY[possible_category["key"]]
    else:
        for key, value in CATEGORY.items():
            if possible_category["value"] in value:
                return CATEGORY[key][possible_category["value"]]
    # print(syns)

    # return json.dumps(syns[0])



    # return json.dumps(category[cate])
    

if __name__ == '__main__':
    app.run(debug=True)
