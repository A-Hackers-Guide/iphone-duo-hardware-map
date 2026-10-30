# `FigDisparityMetadata`

- Image: [`/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`](../userland/System__Library__VideoProcessors__DisparityV5.bundle__DisparityV5.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 33 instance methods, 0 class methods

## Instance variables

```
S _version;
f _baseline;
f _telePixelSizeInMillimeters;
f _widePixelSizeInMillimeters;
@"NSArray" _teleLensDistortionCoefficients;
@"NSArray" _wideLensDistortionCoefficients;
@"NSArray" _teleInverseLensDistortionCoefficients;
@"NSArray" _wideInverseLensDistortionCoefficients;
{CGSize="width"d"height"d} _teleIntrinsicMatrixReferenceDimensions;
{CGSize="width"d"height"d} _wideIntrinsicMatrixReferenceDimensions;
{CGPoint="x"d"y"d} _teleLensDistortionOpticalCenter;
{CGPoint="x"d"y"d} _wideLensDistortionOpticalCenter;
{?="columns"[3]} _teleIntrinsicMatrix;
{?="columns"[3]} _wideIntrinsicMatrix;
{?="columns"[4]} _teleExtrinsicMatrix;
{?="columns"[4]} _wideExtrinsicMatrix;
```

## Properties

```
@property (TS,N,V_version) version;
@property (Tf,N,V_baseline) baseline;
@property (Tf,N,V_telePixelSizeInMillimeters) telePixelSizeInMillimeters;
@property (Tf,N,V_widePixelSizeInMillimeters) widePixelSizeInMillimeters;
@property (T{?=[3]},N,V_teleIntrinsicMatrix) teleIntrinsicMatrix;
@property (T{?=[3]},N,V_wideIntrinsicMatrix) wideIntrinsicMatrix;
@property (T{CGSize=dd},N,V_teleIntrinsicMatrixReferenceDimensions) teleIntrinsicMatrixReferenceDimensions;
@property (T{CGSize=dd},N,V_wideIntrinsicMatrixReferenceDimensions) wideIntrinsicMatrixReferenceDimensions;
@property (T{?=[4]},N,V_teleExtrinsicMatrix) teleExtrinsicMatrix;
@property (T{?=[4]},N,V_wideExtrinsicMatrix) wideExtrinsicMatrix;
@property (T@"NSArray",C,N,V_teleLensDistortionCoefficients) teleLensDistortionCoefficients;
@property (T@"NSArray",C,N,V_wideLensDistortionCoefficients) wideLensDistortionCoefficients;
@property (T@"NSArray",C,N,V_teleInverseLensDistortionCoefficients) teleInverseLensDistortionCoefficients;
@property (T@"NSArray",C,N,V_wideInverseLensDistortionCoefficients) wideInverseLensDistortionCoefficients;
@property (T{CGPoint=dd},N,V_teleLensDistortionOpticalCenter) teleLensDistortionOpticalCenter;
@property (T{CGPoint=dd},N,V_wideLensDistortionOpticalCenter) wideLensDistortionOpticalCenter;
```

## Instance methods

```
-[FigDisparityMetadata version];
-[FigDisparityMetadata baseline];
-[FigDisparityMetadata description];
-[FigDisparityMetadata setVersion:];
-[FigDisparityMetadata setBaseline:];
-[FigDisparityMetadata wideLensDistortionOpticalCenter];
-[FigDisparityMetadata teleLensDistortionOpticalCenter];
-[FigDisparityMetadata teleExtrinsicMatrix];
-[FigDisparityMetadata teleIntrinsicMatrix];
-[FigDisparityMetadata teleIntrinsicMatrixReferenceDimensions];
-[FigDisparityMetadata teleInverseLensDistortionCoefficients];
-[FigDisparityMetadata teleLensDistortionCoefficients];
-[FigDisparityMetadata telePixelSizeInMillimeters];
-[FigDisparityMetadata wideExtrinsicMatrix];
-[FigDisparityMetadata wideIntrinsicMatrix];
-[FigDisparityMetadata wideIntrinsicMatrixReferenceDimensions];
-[FigDisparityMetadata wideInverseLensDistortionCoefficients];
-[FigDisparityMetadata wideLensDistortionCoefficients];
-[FigDisparityMetadata widePixelSizeInMillimeters];
-[FigDisparityMetadata setTeleExtrinsicMatrix:];
-[FigDisparityMetadata setTeleIntrinsicMatrix:];
-[FigDisparityMetadata setTeleIntrinsicMatrixReferenceDimensions:];
-[FigDisparityMetadata setTeleInverseLensDistortionCoefficients:];
-[FigDisparityMetadata setTeleLensDistortionCoefficients:];
-[FigDisparityMetadata setTeleLensDistortionOpticalCenter:];
-[FigDisparityMetadata setTelePixelSizeInMillimeters:];
-[FigDisparityMetadata setWideExtrinsicMatrix:];
-[FigDisparityMetadata setWideIntrinsicMatrix:];
-[FigDisparityMetadata setWideIntrinsicMatrixReferenceDimensions:];
-[FigDisparityMetadata setWideInverseLensDistortionCoefficients:];
-[FigDisparityMetadata setWideLensDistortionCoefficients:];
-[FigDisparityMetadata setWideLensDistortionOpticalCenter:];
-[FigDisparityMetadata setWidePixelSizeInMillimeters:];
```
