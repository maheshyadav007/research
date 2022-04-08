All the experiments are performed with DLGN-SF Protocol.

Notations:

Component 1:
<ul>
  <li>BOTH: Both the NPF and NPV models are trained from epoch 1 to last epoch </li> 
   <li>ONPF: Only NPF model is trained and NPV is freezed </li>
   <li>ONPV: Only NPV model is trained and NPF is freezed </li>
   <li>BOTH_ONPV: Both NPF and NPV models are trained for 2 epochs after that NPF model is freezed and only NPV is trained </li>
</ul>
Component 2: 
<ul>
  <li>PWL: Input data points are given to both NPF and NPV models</li> 
  <li>PWC: Input data is given to only NPF model and the input to NPV is given as all one's</li> 
</ul>
Activation Funcs:
  <ul>
  <li>Soft: Soft ReLU is used </li> 
  <li>Hard: Hard ReLU is used</li> 
  <li>soft_hard: soft ReLU is used for 2 epochs and then hard ReLU is used thereafter </li> 
  </ul>
