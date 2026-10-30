# `FBSDisplayConfigurationRequest`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BSDescriptionProviding`, `NSCopying`, `NSMutableCopying`, `NSSecureCoding`
- 7 instance variables, 11 properties, 21 instance methods, 1 class methods

## Instance variables

```
{CGSize="width"d"height"d} _nativePixelSize;
{CGSize="width"d"height"d} _logicalScale;
d _pointScale;
d _refreshRate;
q _overscanCompensation;
q _hdrMode;
B _disableFrameDoubling;
```

## Properties

```
@property (Tq,R,N,V_overscanCompensation) overscanCompensation;
@property (T{CGSize=dd},R,N,V_nativePixelSize) nativePixelSize;
@property (Td,R,N,V_pointScale) pointScale;
@property (Td,R,N,V_refreshRate) refreshRate;
@property (TB,R,N,V_disableFrameDoubling) disableFrameDoubling;
@property (Tq,R,N,V_hdrMode) hdrMode;
@property (T{CGSize=dd},R,N,V_logicalScale) logicalScale;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSDisplayConfigurationRequest supportsSecureCoding];
```

## Instance methods

```
-[FBSDisplayConfigurationRequest hdrMode];
-[FBSDisplayConfigurationRequest mutableCopyWithZone:];
-[FBSDisplayConfigurationRequest refreshRate];
-[FBSDisplayConfigurationRequest succinctDescriptionBuilder];
-[FBSDisplayConfigurationRequest init];
-[FBSDisplayConfigurationRequest initWithXPCDictionary:];
-[FBSDisplayConfigurationRequest pointScale];
-[FBSDisplayConfigurationRequest logicalScale];
-[FBSDisplayConfigurationRequest descriptionWithMultilinePrefix:];
-[FBSDisplayConfigurationRequest succinctDescription];
-[FBSDisplayConfigurationRequest encodeWithXPCDictionary:];
-[FBSDisplayConfigurationRequest encodeWithCoder:];
-[FBSDisplayConfigurationRequest hash];
-[FBSDisplayConfigurationRequest description];
-[FBSDisplayConfigurationRequest initWithCoder:];
-[FBSDisplayConfigurationRequest nativePixelSize];
-[FBSDisplayConfigurationRequest copyWithZone:];
-[FBSDisplayConfigurationRequest isEqual:];
-[FBSDisplayConfigurationRequest descriptionBuilderWithMultilinePrefix:];
-[FBSDisplayConfigurationRequest disableFrameDoubling];
-[FBSDisplayConfigurationRequest overscanCompensation];
```
