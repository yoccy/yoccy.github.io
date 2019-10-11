from work import Work

def get_work(work_name):
    for work in all_works:
        if work.name == work_name:
            return work
    return None

def get_all_works():
    return all_works

work01 = Work(id=1,
             name="ホームページ",
             image="homepage1.jpg",
             description="このサイトのことです。flaskを使用しました。",
             date="2019年7月##日")

all_works = [work01]