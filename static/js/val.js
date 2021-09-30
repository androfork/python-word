		function number()
		{
		 	var n1 = parseInt(document.getElementById('num').value);
            if(n1<=0)
            {
                alert("number is less than 0");
				document.getElementById("num").style.visibility="visible";
                document.getElementById("num").innerHTML="invalid";
                document.getElementById("num").style.color="red";
                document.getElementById("num").style.visibility="invalids";
                num.style.border="2px solid red";
  
            }
            if(n1>100000)
            {
                alert("the is greater than 1000000")
				document.getElementById("num").style.visibility="visible";
                document.getElementById("num").innerHTML="invalid";
                document.getElementById("num").style.color="red";
                document.getElementById("num").style.visibility="invalids";
                num.style.border="2px solid red";
  
            }
        
			if (document.getElementById("num").value.trim() == "") {
            alert("Please enter Name!");
            return false;
			}
		}