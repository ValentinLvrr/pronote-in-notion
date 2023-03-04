def generate_html(homeworks: dict):
    html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Devoirs</title>
</head>
<body>
"""

    for element in homeworks:
        print(homeworks[element].split('|')[0])
        html += f"""
        <div style="border-color: {homeworks[element].split('|')[0]};"class="homework">
            <h4>{element}</h4>
            <p>{homeworks[element].split('|')[1]}</p>
        </div>"""

    html += """
<style>
body {
    background-color: #fff;
}

div.homework {
    border-style: solid;
    border-width: 10px;
    margin: auto;
    border-radius: 10px;
    background-color: #191919;
    color: #fff;
    text-align: center;
    width: 90%;
    padding-top: 0.1px;
    padding-bottom: 0.1px;
    margin-bottom: 10px;
}
</style>
<script>
const body = document.querySelector('body')
const divs = document.querySelectorAll('.homework')
let darkmode = false
document.addEventListener('keyup', (event) => {
    if (event.key.length === 1) {
      if (darkmode == true) {
        body.style.backgroundColor = "#FFFFFF"
        for (let i = 0; i < divs.length; i++) {
            divs[i].style.backgroundColor = '#191919';
            divs[i].style.color = '#fff';
        }
        darkmode = false
      } else {
        body.style.backgroundColor = "#191919"
        for (let i = 0; i < divs.length; i++) {
            divs[i].style.backgroundColor = '#FFFFFF';
            divs[i].style.color = '#191919';
        }
        darkmode = true
      }
    } 
  })
</script>
</body>
</html>
    """
    open('templates/index.html','w',encoding='utf-8').write(html)
