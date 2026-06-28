let num1 = Number(prompt(" Digite um número: "));
let num2 = Number(prompt(" Digite o segundo número: "));
let num3 = Number(prompt(" Digite o terceiro número: "));
let maior = 0;
let menor = 0;
if(num1>num2 && num1>num3){
    maior = num1;
    console.log(" O maior número é: " + maior);
}

else if(num2>num1 && num2>num3){
    maior = num2;
    console.log(" O maior número é: "+ maior);
}

else{
    maior = num3;
    console.log(" O maior número é: "+ maior);
}
if(num1<num2 && num1<num3){
    menor = num1;
    console.log(" O menor número é: " + menor);
}

else if(num2<num1 && num2<num3){
    menor = num2;
    console.log(" O menor número é: "+ menor);
}

else{
    menor = num3;
    console.log(" O menor número é: "+ menor);
}
