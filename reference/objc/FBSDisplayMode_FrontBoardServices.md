# `FBSDisplayMode`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSSecureCoding`
- 9 instance variables, 10 properties, 32 instance methods, 2 class methods

## Instance variables

```
Q _width;
Q _height;
Q _preferredScale;
d _scaleOverride;
d _refreshRate;
q _gamut;
q _hdr;
q _rotation;
B _virtual;
```

## Properties

```
@property (T{CGSize=dd},R,N) pixelSize;
@property (Td,R,N) pointScale;
@property (T{CGSize=dd},R,N) size;
@property (Td,R,N,V_refreshRate) refreshRate;
@property (Tq,R,N,V_gamut) colorGamut;
@property (Tq,R,N,V_hdr) hdrMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSDisplayMode supportsSecureCoding];
+[FBSDisplayMode _emptyMode];
```

## Instance methods

```
-[FBSDisplayMode hdrMode];
-[FBSDisplayMode refreshRate];
-[FBSDisplayMode init];
-[FBSDisplayMode initWithXPCDictionary:];
-[FBSDisplayMode pointScale];
-[FBSDisplayMode _initWithCADisplayMode:scale:rotation:];
-[FBSDisplayMode _caHDRMode];
-[FBSDisplayMode _initWithWidth:height:preferredScale:scaleOverride:refreshRate:gamut:hdr:rotation:virtual:validityCheck:];
-[FBSDisplayMode pixelSize];
-[FBSDisplayMode _caRefreshRate];
-[FBSDisplayMode size];
-[FBSDisplayMode _copyWithOverrideSize:];
-[FBSDisplayMode _isVirtualMode];
-[FBSDisplayMode scale];
-[FBSDisplayMode colorGamut];
-[FBSDisplayMode encodeWithXPCDictionary:];
-[FBSDisplayMode _copyWithOverrideSize:scale:];
-[FBSDisplayMode _caWidth];
-[FBSDisplayMode _caHeight];
-[FBSDisplayMode encodeWithCoder:];
-[FBSDisplayMode _caColorGamut];
-[FBSDisplayMode hash];
-[FBSDisplayMode description];
-[FBSDisplayMode initWithCoder:];
-[FBSDisplayMode _referenceSizeDescription];
-[FBSDisplayMode nativePixelSize];
-[FBSDisplayMode copyWithZone:];
-[FBSDisplayMode _caPreferredScale];
-[FBSDisplayMode isEqual:];
-[FBSDisplayMode _initWithWidth:height:scale:refreshRate:gamut:hdr:];
-[FBSDisplayMode _rotation];
-[FBSDisplayMode _copyWithOverrideSize:scale:refreshRate:];
```
