Input Data

![Input Data](https://user-images.githubusercontent.com/32334380/138399219-41102d8f-9e53-41f3-a87d-ec40093f5626.png)

Regenerated Data with trained model(MSE  = .003)
![regenerated](https://user-images.githubusercontent.com/32334380/138399484-95e724c0-61c7-445f-94f0-7f128e88721e.png)

Below are the few plots with differnt DNN model initialization and Data points being the same.

Lambda Matrix for Random Init
![arctan2(X _,1 ,X _,0  )(Random) (2)](https://user-images.githubusercontent.com/32334380/138398605-d3b6489b-0794-41a3-950d-a3e8a60ba09d.png)
![arctan2(X _,1 ,X _,0  )(Random) (1)](https://user-images.githubusercontent.com/32334380/138398607-2d63f9c8-dcff-4610-937a-3ae7f7216f47.png)
![arctan2(X _,1 ,X _,0  )(Random)](https://user-images.githubusercontent.com/32334380/138398608-9b91fccc-7ddc-456e-ba4d-538b86691c5e.png)

Lambda Matrix after Learning

![arctan2(X _,1 ,X _,0  )(Learnt) (2)](https://user-images.githubusercontent.com/32334380/138398610-80b6622c-4681-4f98-96c0-5015050c4064.png)
![arctan2(X _,1 ,X _,0  )(Learnt) (1)](https://user-images.githubusercontent.com/32334380/138398613-eb616625-60d6-4c7e-9ab6-9e836ee0ad0f.png)
![arctan2(X _,1 ,X _,0  )(Learnt)](https://user-images.githubusercontent.com/32334380/138398614-64b545b5-6631-4d94-97af-2b2de71a6619.png)

Below are the plot with Data point regenerated
![arctan2(X _,1 ,X _,0  )(Random) (3)](https://user-images.githubusercontent.com/32334380/138398598-efca7434-a0d3-4daa-a18a-346bd4dc484c.png)
![arctan2(X _,1 ,X _,0  )(Learnt) (3)](https://user-images.githubusercontent.com/32334380/138398604-3ba8e003-90a2-48ca-a349-774416ddda2d.png)

Below are the plots of Kernels of each layer(3 layer models)
[K1 - kernel for layer 1,..., K = K1*K2*K3 = Lambda matrix]

![circle_experiment_all](https://user-images.githubusercontent.com/32334380/140611662-6ec6938d-a8eb-467c-8cb8-c59642e27b8d.png)


![K1_arctan2(X _,1 ,X _,0  )(Learnt)](https://user-images.githubusercontent.com/32334380/140611400-0cc0e0f2-30ee-4b33-8d47-82150dad0a6c.png)
![K1_arctan2(X _,1 ,X _,0  )(Learnt)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611401-cfd59e7f-dc86-4acf-97ea-dec7773c19f7.png)
![K1_arctan2(X _,1 ,X _,0  )(Random)](https://user-images.githubusercontent.com/32334380/140611402-7215793d-7186-4271-8106-6c6339f3d763.png)
![K1_arctan2(X _,1 ,X _,0  )(Random)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611403-7cb3de7a-93ab-4976-ac58-b5420854a3a8.png)
![K2_arctan2(X _,1 ,X _,0  )(Learnt)](https://user-images.githubusercontent.com/32334380/140611404-a04cc266-1888-45cd-b47f-5277ceb9cab4.png)
![K2_arctan2(X _,1 ,X _,0  )(Learnt)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611405-4c95c638-fafe-497d-b84c-2cd4377ebbab.png)
![K2_arctan2(X _,1 ,X _,0  )(Random)](https://user-images.githubusercontent.com/32334380/140611406-cbfd345c-830a-419c-a981-33b3b46c26ca.png)
![K2_arctan2(X _,1 ,X _,0  )(Random)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611407-c4fcb311-6379-4f37-8510-2b8b077f3142.png)
![K3_arctan2(X _,1 ,X _,0  )(Learnt)](https://user-images.githubusercontent.com/32334380/140611409-30a3bec3-6b28-453c-a591-0efb684d94b5.png)
![K3_arctan2(X _,1 ,X _,0  )(Learnt)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611410-f0e33058-9439-4aa2-923b-7a1618abbbd2.png)
![K3_arctan2(X _,1 ,X _,0  )(Random)](https://user-images.githubusercontent.com/32334380/140611411-8795ecc5-33d1-47da-ab89-dde6f75f8137.png)
![K3_arctan2(X _,1 ,X _,0  )(Random)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611412-2dd5e32a-e6ec-49f5-92ad-d7ebacb9d256.png)

![K_arctan2(X _,1 ,X _,0  )(Learnt)](https://user-images.githubusercontent.com/32334380/140611395-36e70dc5-2be5-45ff-a7d3-20a71ee40848.png)
![K_arctan2(X _,1 ,X _,0  )(Learnt)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611396-741eacd7-41e9-4ab5-82f2-e8fba4b81ab7.png)
![K_arctan2(X _,1 ,X _,0  )(Random)](https://user-images.githubusercontent.com/32334380/140611397-204bb358-4bc3-40de-9452-45209f06475d.png)
![K_arctan2(X _,1 ,X _,0  )(Random)NPF-NPV Arch](https://user-images.githubusercontent.com/32334380/140611399-536956bc-97bc-4201-bcab-44be4928ab88.png)

Hyperplanes Visualization
![all_hyperplanes](https://user-images.githubusercontent.com/32334380/141240917-be2972e0-dfd5-4c67-ad86-c17d01b06c7c.png)

