# `LLVPreProcessorFrameParameters`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 34 instance variables, 34 properties, 68 instance methods, 0 class methods

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
I _inputLSCGridWidth;
I _inputLSCGridHeight;
f _inputLSCModulationWeight;
I _inputFrameCount;
f _inputNoiseModelGainAnalog;
I _inputNoiseModelwellCapacity;
I _inputNoiseModelConversionGain;
I _inputNoiseModelReadNoise1x;
I _inputNoiseModelReadNoise8x;
^{__CVBuffer=} _inputPixelBufferScale0;
^{__CVBuffer=} _inputPixelBufferScale1;
@"NSArray" _inputLSCArray;
@"NSString" _portType;
Q _quadraBinFactor;
^{__CVBuffer=} _outputPixelBufferScale1;
^{__CVBuffer=} _outputPixelBufferScale2Luma;
^{__CVBuffer=} _outputPixelBufferScale2RGB;
^{__CVBuffer=} _outputPixelBufferNoise;
{CGSize="width"d"height"d} _inputSensorValidDimensions;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputValidRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputSensorArrayOutputRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputSensorReadOutCrop;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputFesCropRect;
```

## Properties

```
@property (T^{__CVBuffer=},N,V_inputPixelBufferScale0) inputPixelBufferScale0;
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
@property (T@"NSString",&,N,V_portType) portType;
@property (TQ,N,V_quadraBinFactor) quadraBinFactor;
@property (T^{__CVBuffer=},N,V_outputPixelBufferScale1) outputPixelBufferScale1;
@property (Tf,N,V_inputNoiseModelGainAnalog) inputNoiseModelGainAnalog;
@property (TI,N,V_inputNoiseModelwellCapacity) inputNoiseModelwellCapacity;
@property (TI,N,V_inputNoiseModelConversionGain) inputNoiseModelConversionGain;
@property (TI,N,V_inputNoiseModelReadNoise1x) inputNoiseModelReadNoise1x;
@property (TI,N,V_inputNoiseModelReadNoise8x) inputNoiseModelReadNoise8x;
@property (T^{__CVBuffer=},N,V_outputPixelBufferScale2Luma) outputPixelBufferScale2Luma;
@property (T^{__CVBuffer=},N,V_outputPixelBufferScale2RGB) outputPixelBufferScale2RGB;
@property (T^{__CVBuffer=},N,V_outputPixelBufferNoise) outputPixelBufferNoise;
@property (T{CGSize=dd},N,V_inputSensorValidDimensions) inputSensorValidDimensions;
```

## Instance methods

```
-[LLVPreProcessorFrameParameters portType];
-[LLVPreProcessorFrameParameters setPortType:];
-[LLVPreProcessorFrameParameters setInputCropRect:];
-[LLVPreProcessorFrameParameters inputCropRect];
-[LLVPreProcessorFrameParameters setInputAWBCombBGain:];
-[LLVPreProcessorFrameParameters setInputAWBCombGGain:];
-[LLVPreProcessorFrameParameters setInputAWBCombRGain:];
-[LLVPreProcessorFrameParameters setInputAWBGrayWorldBGain:];
-[LLVPreProcessorFrameParameters setInputAWBGrayWorldGGain:];
-[LLVPreProcessorFrameParameters setInputAWBGrayWorldRGain:];
-[LLVPreProcessorFrameParameters setInputAWBLocked:];
-[LLVPreProcessorFrameParameters setInputAWBStable:];
-[LLVPreProcessorFrameParameters setInputFesCropRect:];
-[LLVPreProcessorFrameParameters setInputFrameCount:];
-[LLVPreProcessorFrameParameters setInputHrGainDownRatio:];
-[LLVPreProcessorFrameParameters setInputLSCArray:];
-[LLVPreProcessorFrameParameters setInputLSCGridHeight:];
-[LLVPreProcessorFrameParameters setInputLSCGridWidth:];
-[LLVPreProcessorFrameParameters setInputLSCModulationWeight:];
-[LLVPreProcessorFrameParameters setInputPixelBufferScale0:];
-[LLVPreProcessorFrameParameters setInputPixelBufferScale1:];
-[LLVPreProcessorFrameParameters setInputPreIspDGain:];
-[LLVPreProcessorFrameParameters setInputSensorArrayOutputRect:];
-[LLVPreProcessorFrameParameters setInputSensorReadOutCrop:];
-[LLVPreProcessorFrameParameters setInputValidRect:];
-[LLVPreProcessorFrameParameters setOutputPixelBufferScale1:];
-[LLVPreProcessorFrameParameters setQuadraBinFactor:];
-[LLVPreProcessorFrameParameters inputFrameCount];
-[LLVPreProcessorFrameParameters setInputNoiseModelwellCapacity:];
-[LLVPreProcessorFrameParameters setOutputPixelBufferScale2Luma:];
-[LLVPreProcessorFrameParameters quadraBinFactor];
-[LLVPreProcessorFrameParameters inputAWBCombBGain];
-[LLVPreProcessorFrameParameters inputAWBCombGGain];
-[LLVPreProcessorFrameParameters inputAWBCombRGain];
-[LLVPreProcessorFrameParameters inputAWBGrayWorldBGain];
-[LLVPreProcessorFrameParameters inputAWBGrayWorldGGain];
-[LLVPreProcessorFrameParameters inputAWBGrayWorldRGain];
-[LLVPreProcessorFrameParameters inputAWBLocked];
-[LLVPreProcessorFrameParameters inputAWBStable];
-[LLVPreProcessorFrameParameters inputFesCropRect];
-[LLVPreProcessorFrameParameters inputHrGainDownRatio];
-[LLVPreProcessorFrameParameters inputLSCArray];
-[LLVPreProcessorFrameParameters inputLSCGridHeight];
-[LLVPreProcessorFrameParameters inputLSCGridWidth];
-[LLVPreProcessorFrameParameters inputLSCModulationWeight];
-[LLVPreProcessorFrameParameters inputNoiseModelConversionGain];
-[LLVPreProcessorFrameParameters inputNoiseModelGainAnalog];
-[LLVPreProcessorFrameParameters inputNoiseModelReadNoise1x];
-[LLVPreProcessorFrameParameters inputNoiseModelReadNoise8x];
-[LLVPreProcessorFrameParameters inputNoiseModelwellCapacity];
-[LLVPreProcessorFrameParameters inputPixelBufferScale0];
-[LLVPreProcessorFrameParameters inputPixelBufferScale1];
-[LLVPreProcessorFrameParameters inputPreIspDGain];
-[LLVPreProcessorFrameParameters inputSensorArrayOutputRect];
-[LLVPreProcessorFrameParameters inputSensorReadOutCrop];
-[LLVPreProcessorFrameParameters inputSensorValidDimensions];
-[LLVPreProcessorFrameParameters inputValidRect];
-[LLVPreProcessorFrameParameters outputPixelBufferNoise];
-[LLVPreProcessorFrameParameters outputPixelBufferScale1];
-[LLVPreProcessorFrameParameters outputPixelBufferScale2Luma];
-[LLVPreProcessorFrameParameters outputPixelBufferScale2RGB];
-[LLVPreProcessorFrameParameters setInputNoiseModelConversionGain:];
-[LLVPreProcessorFrameParameters setInputNoiseModelGainAnalog:];
-[LLVPreProcessorFrameParameters setInputNoiseModelReadNoise1x:];
-[LLVPreProcessorFrameParameters setInputNoiseModelReadNoise8x:];
-[LLVPreProcessorFrameParameters setInputSensorValidDimensions:];
-[LLVPreProcessorFrameParameters setOutputPixelBufferNoise:];
-[LLVPreProcessorFrameParameters setOutputPixelBufferScale2RGB:];
```
