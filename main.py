import url,store,pursueHtml
import urllib.request

class main:

    def __init__(self):
        self.url = url.url()
        self.store = store.store()
        self.pursueHtml = pursueHtml.pursueHtml()


    def start(self):
        count=1
        while self.url.has_url():
            try:
                #url = 'https://www.renrenche.com/sh/ershouche/p03'
                url = self.url.get_url()
                print(url)
                req = urllib.request.Request(url)

                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
                req.add_header('Host', 'www.renrenche.com')
                req.add_header('Upgrade-Insecure-Requests',1)
                req.add_header('Cookie','antispamWallToken=54a2a3cf269de70ea83799969ee8032bc76d35690fb375de8210ec844545042c; Hm_lvt_16d2464a0f1bb7c6b37e56c3de548f14=1509460294,1509973349; Hm_lpvt_16d2464a0f1bb7c6b37e56c3de548f14=1510152300; antispamWallToken=54a2a3cf269de70ea83799969ee8032bc76d35690fb375de8210ec844545042c; new_visitor_uuid=17d401943354cf1522d7c38e3fe6c5c2; rrc_promo_uuid=rrc_promo_uuid; rrc_promo_two_years=rrc_promo_two_years; zhimai-page-list-banner=true; gifts-show=1510071236290; gifts-show-time=1; popwin-show-time=2; popwin-show=1510072208759; rrc_ip_province=%E4%B8%8A%E6%B5%B7; rrc_modified_city=true; man-left-close=man-left-close; rrc_rrc_session=t5ht4h6c46qggqvpkgjcd6keq1; rrc_rrc_signed=s%2Ct5ht4h6c46qggqvpkgjcd6keq1%2Cac0d15be539a9bd027f7d84fed5f06bd; Hm_lvt_16d2464a0f1bb7c6b37e56c3de548f14=1509460294,1509973349,1510070084,1510138816; Hm_lpvt_16d2464a0f1bb7c6b37e56c3de548f14=1510138816; isLoadPage=loaded; sigma-experiments={"rank-strategy2":"rank2","Add-c1-spider-submitsource":"evaluation"}; rrc_session_city=sh; _ga=GA1.2.1261691474.1509973349; rls_uuid=292F4DFD-E448-4D83-AEB1-39682E49D233; _pzfxuvpc=1509973349006%7C1264200565593700304%7C39%7C1510152300006%7C5%7C7498508710125204144%7C9078424725114582834; _pzfxsvpc=9078424725114582834%7C1510152290932%7C2%7Chttps%3A%2F%2Fwww.renrenche.com%2Fsh%2Fershouche%2F%3Fplog_id%3Df59ece74fff656c3a49bcf5b04855bf7; Hm_lvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1509460294,1509973349,1510070084,1510138816; Hm_lpvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1510152300; rrc_record_city=sh; rrc_fr=bd_pz; rrc_tg=fr%3Dbd_pz%26tg_aid%3D10055728; rrc_ss=initiative')

                respone = urllib.request.urlopen(req)
                print(respone.getcode())
                res = (self.pursueHtml.pursue_list(respone.read().decode('utf-8')))
                store_sign = self.store.store_list(res)

            except Exception as e:
                print('异常处理'+str(count)+str(url)+str(respone.getcode()))
            finally:
                count = count +1


a = main()
a.start()