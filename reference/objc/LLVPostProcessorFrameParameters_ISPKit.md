# `LLVPostProcessorFrameParameters`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 29 instance variables, 29 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _inputAWBStable;
B _inputAWBLocked;
S _inputPreIspDGain;
S _inputAWBCombRGain;
S _inputAWBCombGGain;
S _inputAWBCombBGain;
S _inputAWBGrayWorldRGain;
S _inputAWBGrayWorldGGain;
S _inputAWBGrayWorldBGain;
S _inputHrGainDownRatio;
S _inputAGC;
S _inputSensorDGain;
I _inputLSCGridWidth;
I _inputLSCGridHeight;
f _inputLSCModulationWeight;
I _inputFrameCount;
I _inputIspDGain;
^{__CVBuffer=} _inputPixelBufferScale1;
@"NSArray" _inputLSCArray;
@"NSString" _portType;
Q _quadraBinFactor;
^{__CVBuffer=} _outputPixelBufferScale0;
^{__CVBuffer=} _outputPixelBufferScale1;
{CGSize="width"d"height"d} _inputSensorValidDimensions;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputValidRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputSensorArrayOutputRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputSensorReadOutCrop;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputFesCropRect;
```

## Properties

```
@property (T^{__CVBuffer=},N,V_inputPixelBufferScale1) inputPixelBufferScale1;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputValidRect) inputValidRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputCropRect) inputCropRect;
@property (TI,N,V_inputLSCGridWidth) inputLSCGridWidth;
@property (TI,N,V_inputLSCGridHeight) inputLSCGridHeight;
@property (T@"NSArray",&,N,V_inputLSCArray) inputLSCArray;
@property (Tf,N,V_inputLSCModulationWeight) inputLSCModulationWeight;
@property (TI,N,V_inputFrameCount) inputFrameCount;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputSensorArrayOutputRect) inputSensorArrayOutputRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputSensorReadOutCrop) inputSensorReadOutCrop;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputFesCropRect) inputFesCropRect;
@property (TS,N,V_inputPreIspDGain) inputPreIspDGain;
@property (TS,N,V_inputAWBCombRGain) inputAWBCombRGain;
@property (TS,N,V_inputAWBCombGGain) inputAWBCombGGain;
@property (TS,N,V_inputAWBCombBGain) inputAWBCombBGain;
@property (TS,N,V_inputAWBGrayWorldRGain) inputAWBGrayWorldRGain;
@property (TS,N,V_inputAWBGrayWorldGGain) inputAWBGrayWorldGGain;
@property (TS,N,V_inputAWBGrayWorldBGain) inputAWBGrayWorldBGain;
@property (TB,N,V_inputAWBStable) inputAWBStable;
@property (TB,N,V_inputAWBLocked) inputAWBLocked;
@property (TS,N,V_inputHrGainDownRatio) inputHrGainDownRatio;
@property (TS,N,V_inputAGC) inputAGC;
@property (TI,N,V_inputIspDGain) inputIspDGain;
@property (TS,N,V_inputSensorDGain) inputSensorDGain;
@property (T@"NSString",&,N,V_portType) portType;
@property (TQ,N,V_quadraBinFactor) quadraBinFactor;
@property (T^{__CVBuffer=},N,V_outputPixelBufferScale0) outputPixelBufferScale0;
@property (T^{__CVBuffer=},N,V_outputPixelBufferScale1) outputPixelBufferScale1;
@property (T{CGSize=dd},N,V_inputSensorValidDimensions) inputSensorValidDimensions;
```

## Instance methods

```
-[LLVPostProcessorFrameParameters portType];
-[LLVPostProcessorFrameParameters setPortType:];
-[LLVPostProcessorFrameParameters setInputCropRect:];
-[LLVPostProcessorFrameParameters inputCropRect];
-[LLVPostProcessorFrameParameters setInputAGC:];
-[LLVPostProcessorFrameParameters setInputAWBCombBGain:];
-[LLVPostProcessorFrameParameters setInputAWBCombGGain:];
-[LLVPostProcessorFrameParameters setInputAWBCombRGain:];
-[LLVPostProcessorFrameParameters setInputAWBGrayWorldBGain:];
-[LLVPostProcessorFrameParameters setInputAWBGrayWorldGGain:];
-[LLVPostProcessorFrameParameters setInputAWBGrayWorldRGain:];
-[LLVPostProcessorFrameParameters setInputAWBLocked:];
-[LLVPostProcessorFrameParameters setInputAWBStable:];
-[LLVPostProcessorFrameParameters setInputFesCropRect:];
-[LLVPostProcessorFrameParameters setInputFrameCount:];
-[LLVPostProcessorFrameParameters setInputHrGainDownRatio:];
-[LLVPostProcessorFrameParameters setInputIspDGain:];
-[LLVPostProcessorFrameParameters setInputLSCArray:];
-[LLVPostProcessorFrameParameters setInputLSCGridHeight:];
-[LLVPostProcessorFrameParameters setInputLSCGridWidth:];
-[LLVPostProcessorFrameParameters setInputLSCModulationWeight:];
-[LLVPostProcessorFrameParameters setInputPixelBufferScale1:];
-[LLVPostProcessorFrameParameters setInputPreIspDGain:];
-[LLVPostProcessorFrameParameters setInputSensorArrayOutputRect:];
-[LLVPostProcessorFrameParameters setInputSensorDGain:];
-[LLVPostProcessorFrameParameters setInputSensorReadOutCrop:];
-[LLVPostProcessorFrameParameters setInputValidRect:];
-[LLVPostProcessorFrameParameters setOutputPixelBufferScale0:];
-[LLVPostProcessorFrameParameters setOutputPixelBufferScale1:];
-[LLVPostProcessorFrameParameters setQuadraBinFactor:];
-[LLVPostProcessorFrameParameters inputFrameCount];
-[LLVPostProcessorFrameParameters quadraBinFactor];
-[LLVPostProcessorFrameParameters inputAGC];
-[LLVPostProcessorFrameParameters inputAWBCombBGain];
-[LLVPostProcessorFrameParameters inputAWBCombGGain];
-[LLVPostProcessorFrameParameters inputAWBCombRGain];
-[LLVPostProcessorFrameParameters inputAWBGrayWorldBGain];
-[LLVPostProcessorFrameParameters inputAWBGrayWorldGGain];
-[LLVPostProcessorFrameParameters inputAWBGrayWorldRGain];
-[LLVPostProcessorFrameParameters inputAWBLocked];
-[LLVPostProcessorFrameParameters inputAWBStable];
-[LLVPostProcessorFrameParameters inputFesCropRect];
-[LLVPostProcessorFrameParameters inputHrGainDownRatio];
-[LLVPostProcessorFrameParameters inputIspDGain];
-[LLVPostProcessorFrameParameters inputLSCArray];
-[LLVPostProcessorFrameParameters inputLSCGridHeight];
-[LLVPostProcessorFrameParameters inputLSCGridWidth];
-[LLVPostProcessorFrameParameters inputLSCModulationWeight];
-[LLVPostProcessorFrameParameters inputPixelBufferScale1];
-[LLVPostProcessorFrameParameters inputPreIspDGain];
-[LLVPostProcessorFrameParameters inputSensorArrayOutputRect];
-[LLVPostProcessorFrameParameters inputSensorDGain];
-[LLVPostProcessorFrameParameters inputSensorReadOutCrop];
-[LLVPostProcessorFrameParameters inputSensorValidDimensions];
-[LLVPostProcessorFrameParameters inputValidRect];
-[LLVPostProcessorFrameParameters outputPixelBufferScale0];
-[LLVPostProcessorFrameParameters outputPixelBufferScale1];
-[LLVPostProcessorFrameParameters setInputSensorValidDimensions:];
```
