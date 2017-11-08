import url,store,pursueHtml
import urllib.request

class main:

    def __init__(self):
        self.url = url.url()
        self.store = store.store()
        self.pursueHtml = pursueHtml.pursueHtml()


    def start(self):
        count=1
        #while self.url.has_url():
        while count<2:
           # try:
                url = 'https://www.renrenche.com/sh/ershouche/p03'
                #url = self.url.get_url()

                req = urllib.request.Request(url)

                req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
                req.add_header('Host', 'www.renrenche.com')
                req.add_header('Upgrade-Insecure-Requests',1)
                req.add_header('Cookie','Hm_lvt_16d2464a0f1bb7c6b37e56c3de548f14=1507702033; Hm_lpvt_16d2464a0f1bb7c6b37e56c3de548f14=1510127711; antispamWallToken=715ffde6526149e5d9363eadd06f91adf2c09f985342f54ae509dbe7219d0c06; new_visitor_uuid=a7c18c592213a5162eedf79079af8038; rrc_promo_two_years=rrc_promo_two_years; rrc_promo_uuid=rrc_promo_uuid; zhimai-page-list-banner=true; rrc_ip_city_twohour=sh; sigma-experiments={"rank-strategy2":"rank2","Add-c1-spider-submitsource":"control-group"}; rrc_rrc_session=mi9s7tebtg5l6ihnc8200sesv2; rrc_rrc_signed=s%2Cmi9s7tebtg5l6ihnc8200sesv2%2Cc7921c34e37a216a80e437b09358dc91; isLoadPage=loaded; _gat=1; Hm_lvt_16d2464a0f1bb7c6b37e56c3de548f14=1510122820,1510125391,1510126601,1510127704; Hm_lpvt_16d2464a0f1bb7c6b37e56c3de548f14=1510127704; LXB_REFER=bzclk.baidu.com; rrc_tg=fr%3Dbd_pz%26tg_aid%3D10055728; rrc_session_city=sh; _ga=GA1.2.761494701.1507702032; rls_uuid=B7CD3098-7CEE-470E-A5B4-3E4EA57FA28F; _pzfxuvpc=1507702032367%7C1371730763223975471%7C23%7C1510127710912%7C5%7C6358152985206514393%7C2097610535212510977; _pzfxsvpc=2097610535212510977%7C1510125390256%7C7%7Chttp%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00fAG29_0gyuu0PIxI0K2osFp00000KNAxNb00000uND48Z.THLcztWQ_eR0UWdBmy-bIfK15HbLnHT4mH7Bnj0snAu-mhD0IHdafWbYfYwAwRPDwjPAPWTvrjbsfYnznW63rHT4fbnLw6K95gTqFhdWpyfqn10vnj0dnWRzrausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4zuy4zuy4WpAR8mvqVQ1qhTWdBu7qsXBuYudq9pyfqnH0sPHRLnW60mLFW5Hf1nW61%26tpl%3Dtpl_10086_15727_11221%26l%3D1501382165%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E4%2525BA%2525BA%2525E4%2525BA%2525BA%2525E8%2525BD%2525A6%2525E4%2525BA%25258C%2525E6%252589%25258B%2525E8%2525BD%2525A6%2525E3%252580%252591%2525E7%25259B%2525B4%2525E5%25258D%252596%2525E8%25258A%252582%2525E6%25259D%2525A5%2525E8%2525A2%2525AD%25252C%2525E5%25258D%252596%2525E8%2525BD%2525A6%2526xp%253Did(%252522m692fb726%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D240%26ie%3DUTF-8%26f%3D8%26tn%3Dbaidu%26wd%3D%25E4%25BA%25BA%25E4%25BA%25BA%25E8%25BD%25A6%26oq%3D%25E4%25BA%25BA%25E4%25BA%25BA%25E8%25BD%25A6%26rqlang%3Dcn; Hm_lvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1510122820,1510125391,1510126601,1510127704; Hm_lpvt_c8b7b107a7384eb2ad1c1e2cf8c62dbe=1510127711; rrc_ip_province=%E4%B8%8A%E6%B5%B7; rrc_record_city=sh; rrc_fr=bd_pz; rrc_ss=initiative')

                respone = urllib.request.urlopen(req)


                print(respone.getcode())
                #print(respone.read().decode('utf-8'))
                print(self.pursueHtml.pursue_list(respone.read().decode('utf-8')))
          #  except Exception:
                print('异常处理'+str(count))
          #  else:
                count = count +1


a = main()
a.start()