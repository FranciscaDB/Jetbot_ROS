# Usage Explanation

It is strongly recommended to first play with the various examples that come by default with the JetBot image.

## Road Following 

In short, the idea is to execute a flow of code:

1. 1_data_collection.ipynb

2. 2_train_model.ipynb

3. Live demo
   - Option 1: 3a_live_demo.ipynb 
   - Option 2: 3b_1_live_demo_build_trt.ipynb -> Optimize the model using TensorRT
   
   If you choose **Option 2**:
   - Option 2.1: 3b_2_live_demo_trt.ipynb -> To control just one JetBot
   - Option 2.2: Platooning_Leader.ipynb or Platooning _NX.ipynb -> These codes use MQTT to enable communication 

Platooning_Leader.ipynb runs on the jetbot that will be controlled through the GUI, while Platooning_NX.ipynb, with X = jetbot number, will be executed on the jetbot that will receive inputs via MQTT.

## How to configure the parameters in Platooning_*.ipynb

es necesario configurar el broker de MQTT
IP de cada dispositivo
