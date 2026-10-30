# `LLVProcessorFrameParameters`

- Image: [`/System/Library/PrivateFrameworks/ISPKit.framework/ISPKit`](../userland/System__Library__PrivateFrameworks__ISPKit.framework__ISPKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 35 instance variables, 35 properties, 70 instance methods, 0 class methods

## Instance variables

```
B _inputClearHistory;
B _inputAWBStable;
B _inputAWBLocked;
S _inputAGC;
S _inputSensorDGain;
S _inputPreIspDGain;
S _inputAWBCombRGain;
S _inputAWBCombGGain;
S _inputAWBCombBGain;
S _inputAWBGrayWorldRGain;
S _inputAWBGrayWorldGGain;
S _inputAWBGrayWorldBGain;
I _inputFrameCount;
I _inputFesOutputWidth;
I _inputFesOutputHeight;
f _inputImageRegistrationGyroHomographyConfidence;
i _inputImageRegistrationStatus;
f _inputImageRegistrationInliersConfidence;
f _inputExposureTime;
f _inputFNumber;
I _inputIspDGain;
^{__CVBuffer=} _inputPixelBuffer;
^{__CVBuffer=} _inputHumanFullBodiesMaskPixelBuffer;
@"NSString" _portType;
Q _quadraBinFactor;
^{__CVBuffer=} _outputPixelBuffer;
^{__CVBuffer=} _inputPixelBufferNoise;
^{__CVBuffer=} _inputPixelBufferScale2Luma;
^{__CVBuffer=} _inputPixelBufferScale2RGB;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputValidRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputSensorReadOutCrop;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputFesCropRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputSensorArrayOutputRect;
{?="columns"[3]} _inputWarpMatrix;
```

## Properties

```
@property (T^{__CVBuffer=},N,V_inputPixelBuffer) inputPixelBuffer;
@property (T^{__CVBuffer=},N,V_inputHumanFullBodiesMaskPixelBuffer) inputHumanFullBodiesMaskPixelBuffer;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputValidRect) inputValidRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputCropRect) inputCropRect;
@property (TB,N,V_inputClearHistory) inputClearHistory;
@property (TI,N,V_inputFrameCount) inputFrameCount;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputSensorReadOutCrop) inputSensorReadOutCrop;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputFesCropRect) inputFesCropRect;
@property (TI,N,V_inputFesOutputWidth) inputFesOutputWidth;
@property (TI,N,V_inputFesOutputHeight) inputFesOutputHeight;
@property (T@"NSString",&,N,V_portType) portType;
@property (TQ,N,V_quadraBinFactor) quadraBinFactor;
@property (T{?=[3]},N,V_inputWarpMatrix) inputWarpMatrix;
@property (Tf,N,V_inputImageRegistrationGyroHomographyConfidence) inputImageRegistrationGyroHomographyConfidence;
@property (Ti,N,V_inputImageRegistrationStatus) inputImageRegistrationStatus;
@property (Tf,N,V_inputImageRegistrationInliersConfidence) inputImageRegistrationInliersConfidence;
@property (Tf,N,V_inputExposureTime) inputExposureTime;
@property (Tf,N,V_inputFNumber) inputFNumber;
@property (TS,N,V_inputAGC) inputAGC;
@property (TI,N,V_inputIspDGain) inputIspDGain;
@property (TS,N,V_inputSensorDGain) inputSensorDGain;
@property (TS,N,V_inputPreIspDGain) inputPreIspDGain;
@property (TS,N,V_inputAWBCombRGain) inputAWBCombRGain;
@property (TS,N,V_inputAWBCombGGain) inputAWBCombGGain;
@property (TS,N,V_inputAWBCombBGain) inputAWBCombBGain;
@property (TS,N,V_inputAWBGrayWorldRGain) inputAWBGrayWorldRGain;
@property (TS,N,V_inputAWBGrayWorldGGain) inputAWBGrayWorldGGain;
@property (TS,N,V_inputAWBGrayWorldBGain) inputAWBGrayWorldBGain;
@property (TB,N,V_inputAWBStable) inputAWBStable;
@property (TB,N,V_inputAWBLocked) inputAWBLocked;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_inputSensorArrayOutputRect) inputSensorArrayOutputRect;
@property (T^{__CVBuffer=},N,V_outputPixelBuffer) outputPixelBuffer;
@property (T^{__CVBuffer=},N,V_inputPixelBufferNoise) inputPixelBufferNoise;
@property (T^{__CVBuffer=},N,V_inputPixelBufferScale2Luma) inputPixelBufferScale2Luma;
@property (T^{__CVBuffer=},N,V_inputPixelBufferScale2RGB) inputPixelBufferScale2RGB;
```

## Instance methods

```
-[LLVProcessorFrameParameters outputPixelBuffer];
-[LLVProcessorFrameParameters setInputPixelBuffer:];
-[LLVProcessorFrameParameters inputPixelBuffer];
-[LLVProcessorFrameParameters setOutputPixelBuffer:];
-[LLVProcessorFrameParameters portType];
-[LLVProcessorFrameParameters setPortType:];
-[LLVProcessorFrameParameters setInputCropRect:];
-[LLVProcessorFrameParameters inputCropRect];
-[LLVProcessorFrameParameters setInputAGC:];
-[LLVProcessorFrameParameters setInputAWBCombBGain:];
-[LLVProcessorFrameParameters setInputAWBCombGGain:];
-[LLVProcessorFrameParameters setInputAWBCombRGain:];
-[LLVProcessorFrameParameters setInputAWBGrayWorldBGain:];
-[LLVProcessorFrameParameters setInputAWBGrayWorldGGain:];
-[LLVProcessorFrameParameters setInputAWBGrayWorldRGain:];
-[LLVProcessorFrameParameters setInputAWBLocked:];
-[LLVProcessorFrameParameters setInputAWBStable:];
-[LLVProcessorFrameParameters setInputClearHistory:];
-[LLVProcessorFrameParameters setInputExposureTime:];
-[LLVProcessorFrameParameters setInputFNumber:];
-[LLVProcessorFrameParameters setInputFesCropRect:];
-[LLVProcessorFrameParameters setInputFesOutputHeight:];
-[LLVProcessorFrameParameters setInputFesOutputWidth:];
-[LLVProcessorFrameParameters setInputFrameCount:];
-[LLVProcessorFrameParameters setInputHumanFullBodiesMaskPixelBuffer:];
-[LLVProcessorFrameParameters setInputImageRegistrationGyroHomographyConfidence:];
-[LLVProcessorFrameParameters setInputImageRegistrationInliersConfidence:];
-[LLVProcessorFrameParameters setInputImageRegistrationStatus:];
-[LLVProcessorFrameParameters setInputIspDGain:];
-[LLVProcessorFrameParameters setInputPreIspDGain:];
-[LLVProcessorFrameParameters setInputSensorArrayOutputRect:];
-[LLVProcessorFrameParameters setInputSensorDGain:];
-[LLVProcessorFrameParameters setInputSensorReadOutCrop:];
-[LLVProcessorFrameParameters setInputValidRect:];
-[LLVProcessorFrameParameters setInputWarpMatrix:];
-[LLVProcessorFrameParameters setQuadraBinFactor:];
-[LLVProcessorFrameParameters inputFrameCount];
-[LLVProcessorFrameParameters inputWarpMatrix];
-[LLVProcessorFrameParameters quadraBinFactor];
-[LLVProcessorFrameParameters inputAGC];
-[LLVProcessorFrameParameters inputAWBCombBGain];
-[LLVProcessorFrameParameters inputAWBCombGGain];
-[LLVProcessorFrameParameters inputAWBCombRGain];
-[LLVProcessorFrameParameters inputAWBGrayWorldBGain];
-[LLVProcessorFrameParameters inputAWBGrayWorldGGain];
-[LLVProcessorFrameParameters inputAWBGrayWorldRGain];
-[LLVProcessorFrameParameters inputAWBLocked];
-[LLVProcessorFrameParameters inputAWBStable];
-[LLVProcessorFrameParameters inputClearHistory];
-[LLVProcessorFrameParameters inputExposureTime];
-[LLVProcessorFrameParameters inputFNumber];
-[LLVProcessorFrameParameters inputFesCropRect];
-[LLVProcessorFrameParameters inputFesOutputHeight];
-[LLVProcessorFrameParameters inputFesOutputWidth];
-[LLVProcessorFrameParameters inputHumanFullBodiesMaskPixelBuffer];
-[LLVProcessorFrameParameters inputImageRegistrationGyroHomographyConfidence];
-[LLVProcessorFrameParameters inputImageRegistrationInliersConfidence];
-[LLVProcessorFrameParameters inputImageRegistrationStatus];
-[LLVProcessorFrameParameters inputIspDGain];
-[LLVProcessorFrameParameters inputPixelBufferNoise];
-[LLVProcessorFrameParameters inputPixelBufferScale2Luma];
-[LLVProcessorFrameParameters inputPixelBufferScale2RGB];
-[LLVProcessorFrameParameters inputPreIspDGain];
-[LLVProcessorFrameParameters inputSensorArrayOutputRect];
-[LLVProcessorFrameParameters inputSensorDGain];
-[LLVProcessorFrameParameters inputSensorReadOutCrop];
-[LLVProcessorFrameParameters inputValidRect];
-[LLVProcessorFrameParameters setInputPixelBufferNoise:];
-[LLVProcessorFrameParameters setInputPixelBufferScale2Luma:];
-[LLVProcessorFrameParameters setInputPixelBufferScale2RGB:];
```
