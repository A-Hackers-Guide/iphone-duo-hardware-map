# `BLSHPresentationDateSpecifier`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSPresentationDateSpecifying`
- 5 instance variables, 9 properties, 14 instance methods, 2 class methods

## Instance variables

```
Q _encodedPresentationTime;
@"NSDate" _presentationDate;
@"NSArray" _specifiers;
Q _lowPowerRenderingPresentationTime;
q _sourceFrameType;
```

## Properties

```
@property (T@"NSDate",R,N,V_presentationDate) presentationDate;
@property (TQ,R,N) encodedPresentationTime;
@property (T@"NSArray",R,N,V_specifiers) specifiers;
@property (TQ,R,N,V_lowPowerRenderingPresentationTime) lowPowerRenderingPresentationTime;
@property (Tq,R,N,V_sourceFrameType) sourceFrameType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHPresentationDateSpecifier specifierWithPresentationDate:specifiers:];
+[BLSHPresentationDateSpecifier specifierWithPresentationDate:specifiers:lowPowerRenderingPresentationTime:sourceFrameType:];
```

## Instance methods

```
-[BLSHPresentationDateSpecifier bls_loggingString];
-[BLSHPresentationDateSpecifier bls_shortLoggingString];
-[BLSHPresentationDateSpecifier filter:];
-[BLSHPresentationDateSpecifier hash];
-[BLSHPresentationDateSpecifier description];
-[BLSHPresentationDateSpecifier presentationDate];
-[BLSHPresentationDateSpecifier isEqual:];
-[BLSHPresentationDateSpecifier lowPowerRenderingPresentationTime];
-[BLSHPresentationDateSpecifier specifiers];
-[BLSHPresentationDateSpecifier sourceFrameType];
-[BLSHPresentationDateSpecifier dateSpecifierForEnvironment:];
-[BLSHPresentationDateSpecifier encodedPresentationTime];
-[BLSHPresentationDateSpecifier enumerateDateSpecifiersUsingBlock:];
-[BLSHPresentationDateSpecifier initWithPresentationDate:specifiers:lowPowerRenderingPresentationTime:sourceFrameType:];
```
