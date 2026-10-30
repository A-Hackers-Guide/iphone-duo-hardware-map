# `BWPointCloudFormatRequirements`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWFormatRequirements`
- Protocols: `NSSecureCoding`
- 4 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
Q _maxPoints;
Q _dataBufferSize;
@"NSArray" _supportedDataFormats;
B _memoryPoolUseAllowed;
```

## Properties

```
@property (T@"NSArray",C,N,V_supportedDataFormats) supportedDataFormats;
@property (TQ,N,V_maxPoints) maxPoints;
@property (TQ,N,V_dataBufferSize) dataBufferSize;
@property (T@"NSDictionary",R,N) dataBufferAttributes;
@property (TB,N,V_memoryPoolUseAllowed) memoryPoolUseAllowed;
```

## Class methods

```
+[BWPointCloudFormatRequirements supportsSecureCoding];
```

## Instance methods

```
-[BWPointCloudFormatRequirements init];
-[BWPointCloudFormatRequirements dealloc];
-[BWPointCloudFormatRequirements memoryPoolUseAllowed];
-[BWPointCloudFormatRequirements encodeWithCoder:];
-[BWPointCloudFormatRequirements hash];
-[BWPointCloudFormatRequirements description];
-[BWPointCloudFormatRequirements initWithCoder:];
-[BWPointCloudFormatRequirements formatClass];
-[BWPointCloudFormatRequirements mediaType];
-[BWPointCloudFormatRequirements isEqual:];
-[BWPointCloudFormatRequirements setMemoryPoolUseAllowed:];
-[BWPointCloudFormatRequirements dataBufferAttributes];
-[BWPointCloudFormatRequirements dataBufferSize];
-[BWPointCloudFormatRequirements maxPoints];
-[BWPointCloudFormatRequirements setDataBufferSize:];
-[BWPointCloudFormatRequirements setMaxPoints:];
-[BWPointCloudFormatRequirements setSupportedDataFormats:];
-[BWPointCloudFormatRequirements supportedDataFormats];
```
