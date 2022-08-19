from flask import Flask, request, render_template, send_from_directory
from main import share, base_price, plot_graph, cal_graph_values, pos_neg, con_count,clustering

app = Flask(__name__)
page = 'main.html'


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


@app.route('/share_search', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        Share_name_input1 = request.form.get("sname")
        Share_name_input, share_nam, count, total1, output, out, pl_1 = share(Share_name_input1)
        bas_val = base_price(Share_name_input,share_nam)
        a, b, values1 = cal_graph_values(bas_val, count, total1)
        nxt_line = f"<br>"

        fgf1 = fgf(pl_1)
        graph_result1 = f"<img src='data:image/png;base64,{fgf1}'/>"

        gra = plot_graph(bas_val, a, b, values1)
        graph_result = f"<img src='data:image/png;base64,{gra}'/>"

        gra2 = con_count(pl_1)
        graph_result2 = f"<img src='data:image/png;base64,{gra2}'/>"

        a = clustering(pl_1)
        a1 = b1 = c1 = ''
        for i in range(0,len(a)):
            if(i<25):
                a1 = a1 + "\n" + a[i] + ","
            elif(i>25 and i<50):
                b1 = b1 + "\n" + a[i]+ ","
            else:
                c1 = c1 + "\n" + a[i]+ ","
        return f"<h4>" + "Company Name = " + f"</h4>" + Share_name_input1 + " : " + share_nam + nxt_line + \
               f"<h4>" + "Predicted Price Graph =  " + f"</h4>" + graph_result + nxt_line + \
               f"<h4>" + "Most common Words =  " + f"</h4>" + graph_result2 + nxt_line + \
               f"<h4>" + "Pos-Neg Graph =  " + f"</h4>" + graph_result1 + nxt_line + \
               f"<h4>" + "Top terms per cluster: " + f"</h4>" + \
               f"<h5>" + "Cluster 1 = " + f"</h5>" + a1 + nxt_line + \
               f"<h5>" + "Cluster 2 = " + f"</h5>" + b1 + nxt_line + \
               f"<h5>" + "Cluster 3 = " + f"</h5>" + c1 + nxt_line + nxt_line + \
               f"<h4>" + "Related Articles = " + f"</h4>" + nxt_line + out
    return render_template("abc.html")


@app.route('/')
def gff():
    return render_template('main.html')


@app.route('/b_html')
def b_html():
    return render_template('1.html')


@app.route('/main.html')
def main1():
    return render_template('main.html')


def fgf(pl_1):
    print("import graph from pos_neg")
    gra = pos_neg(pl_1)
    return gra


if __name__ == '__main__':
    app.run()
