# `RAWConvert`

- Image: [`/System/Library/CoreServices/RawCamera.bundle/RawCamera`](../userland/System__Library__CoreServices__RawCamera.bundle__RawCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `RAWFilter`
- 20 instance variables, 1 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"CIImage" inputImage;
@ inputColorSpace;
@"NSArray" inputNeutral;
@"NSNumber" inputRange;
@"NSNumber" inputFactor;
@"NSNumber" inputCalibrationIlluminant1;
@"NSNumber" inputCalibrationIlluminant2;
@"NSArray" inputXYZtoCamera1;
@"NSArray" inputXYZtoCamera2;
@"NSArray" inputCameraCalibration1;
@"NSArray" inputCameraCalibration2;
@"NSArray" inputReduction1;
@"NSArray" inputReduction2;
@"NSArray" inputForwardMatrix1;
@"NSArray" inputForwardMatrix2;
@"NSNumber" inputShouldUseForwardMatrix;
@"NSNumber" inputShouldRecoverHighlights;
@"NSNumber" inputShouldLinearize;
@"CIVector" inputBlacks;
@"NSNumber" inputTargetRange;
```

## Properties

```
@property (T{CCameraProfile=^^?ii{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}S{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}{CMatrix=II{vector<double, std::allocator<double>>=^d^d{?=^d}}}},R,N) cameraProfile;
```

## Class methods

```
+[RAWConvert customAttributes];
+[RAWConvert automaticallyNotifiesObserversForKey:];
```

## Instance methods

```
-[RAWConvert customAttributes];
-[RAWConvert outputImage];
-[RAWConvert blendFactor];
-[RAWConvert cameraProfile];
-[RAWConvert setInputNeutral:];
-[RAWConvert inputNeutralXY];
-[RAWConvert matrixFromArray:rowCount:columnCount:];
-[RAWConvert neutralWhitePointWithProfile:];
-[RAWConvert outputMatrix];
```
