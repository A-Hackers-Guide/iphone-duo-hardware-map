# `MLFeatureValue`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 11 properties, 28 instance methods, 24 class methods

## Instance variables

```
B _undefined;
q _type;
@ _value;
@"NSObject" _objectValue;
```

## Properties

```
@property (T@,&,V_value) value;
@property (T@"NSObject",&,N,V_objectValue) objectValue;
@property (Tq,R,N,V_type) type;
@property (TB,R,N,GisUndefined,V_undefined) undefined;
@property (Tq,R,N) int64Value;
@property (Td,R,N) doubleValue;
@property (T@"NSString",R,C,N) stringValue;
@property (T@"MLMultiArray",R,N) multiArrayValue;
@property (T@"NSDictionary",R,N) dictionaryValue;
@property (T^{__CVBuffer=},R,N) imageBufferValue;
@property (T@"MLSequence",R,N) sequenceValue;
```

## Class methods

```
+[MLFeatureValue supportsSecureCoding];
+[MLFeatureValue featureValueWithState:];
+[MLFeatureValue featureValueWithCGImage:pixelsWide:pixelsHigh:pixelFormatType:options:error:];
+[MLFeatureValue featureValueWithCGImage:constraint:options:error:];
+[MLFeatureValue featureValueWithSequence:];
+[MLFeatureValue featureValueWithInt64:];
+[MLFeatureValue featureValueWithImageAtURL:pixelsWide:pixelsHigh:pixelFormatType:options:error:];
+[MLFeatureValue internalFeatureValueWithState:];
+[MLFeatureValue featureValueWithImageAtURL:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:error:];
+[MLFeatureValue featureValueWithCGImage:orientation:pixelsWide:pixelsHigh:pixelFormatType:options:error:];
+[MLFeatureValue featureValueWithMultiArray:];
+[MLFeatureValue featureValueWithDictionary:error:];
+[MLFeatureValue visionCropAndScaleOptionFromOptions:];
+[MLFeatureValue featureValueWithImageAtURL:orientation:constraint:options:error:];
+[MLFeatureValue undefinedFeatureValueWithType:];
+[MLFeatureValue cropRectFromOptions:];
+[MLFeatureValue featureValueWithDouble:];
+[MLFeatureValue featureValueWithInt64KeyDictionary:];
+[MLFeatureValue featureValueOfType:fromObject:error:];
+[MLFeatureValue featureValueWithString:];
+[MLFeatureValue featureValueWithStringKeyDictionary:];
+[MLFeatureValue featureValueWithPixelBuffer:];
+[MLFeatureValue featureValueWithCGImage:orientation:constraint:options:error:];
+[MLFeatureValue featureValueWithImageAtURL:constraint:options:error:];
```

## Instance methods

```
-[MLFeatureValue stringValue];
-[MLFeatureValue objectValue];
-[MLFeatureValue int64Value];
-[MLFeatureValue dictionaryValue];
-[MLFeatureValue doubleValue];
-[MLFeatureValue sequenceValue];
-[MLFeatureValue getFeatureSize:];
-[MLFeatureValue debugQuickLookObject];
-[MLFeatureValue dealloc];
-[MLFeatureValue value];
-[MLFeatureValue isUndefined];
-[MLFeatureValue setValue:];
-[MLFeatureValue type];
-[MLFeatureValue setObjectValue:];
-[MLFeatureValue encodeWithCoder:];
-[MLFeatureValue hash];
-[MLFeatureValue description];
-[MLFeatureValue initWithValue:type:];
-[MLFeatureValue initWithUndefinedValueAndType:];
-[MLFeatureValue initWithCoder:];
-[MLFeatureValue getFeatureSize:ndArrayMode:];
-[MLFeatureValue multiArrayValue];
-[MLFeatureValue copyWithZone:];
-[MLFeatureValue internalStateValue];
-[MLFeatureValue isEqual:];
-[MLFeatureValue imageBufferValue];
-[MLFeatureValue stateValue];
-[MLFeatureValue isEqualToFeatureValue:];
```
