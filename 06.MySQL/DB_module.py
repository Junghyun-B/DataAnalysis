import pymysql

# 월별 매출/이익
def get_monthly_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT DATE_FORMAT(sdate, '%m') AS `month`, 
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `month`
            ORDER BY `month`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 거래처별 매출/이익
def get_company_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany, 
            SUM(revenue) AS revenue, SUM(profit) AS profit
            FROM sales_book
            GROUP BY `scompany`;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 거래처별 판매제품 및 수량
def get_comname_by_company(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT scompany, pname, SUM(sunit) AS unit
            FROM sales_book
            GROUP BY scompany, pname
            ORDER BY scompany;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 신한은행
def get_company1_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname, sum(sunit)
            FROM sales_book
            WHERE scompany='신한은행'
            GROUP BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 국민은행
def get_company2_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname, sum(sunit)
            FROM sales_book
            WHERE scompany='국민은행'
            GROUP BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 우리은행
def get_company3_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname, sum(sunit)
            FROM sales_book
            WHERE scompany='우리은행'
            GROUP BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 기업은행
def get_company4_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname, sum(sunit)
            FROM sales_book
            WHERE scompany='기업은행'
            GROUP BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 하나은행
def get_company5_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname, sum(sunit)
            FROM sales_book
            WHERE scompany='하나은행'
            GROUP BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 제품별 판매수량/매출/이익
def get_name_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pname, SUM(sunit) AS sunit,
	        SUM(revenue) AS revenue, SUM(profit) as profit
	        FROM sales_book
	        GROUP BY pname;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results

# 카테고리별 매출/이익
def get_category_data(config):
    conn = pymysql.connect(**config)
    cur = conn.cursor()

    sql = """
        SELECT pcategory,
	        SUM(revenue) AS revenue, SUM(profit) as profit
            FROM sales_book
            GROUP BY pcategory;
    """
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results