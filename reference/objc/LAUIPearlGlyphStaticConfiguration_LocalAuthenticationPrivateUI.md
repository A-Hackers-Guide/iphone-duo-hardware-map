# `LAUIPearlGlyphStaticConfiguration`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 2 class methods

## Instance variables

```
B _secureVariantEnabled;
B _recording;
q _initialStyle;
q _pathStyle;
d _lineThicknessScale;
d _checkmarkThicknessScale;
q _secureVariantType;
```

## Properties

```
@property (Tq,N,V_initialStyle) initialStyle;
@property (Tq,N,V_pathStyle) pathStyle;
@property (Td,N,V_lineThicknessScale) lineThicknessScale;
@property (Td,N,V_checkmarkThicknessScale) checkmarkThicknessScale;
@property (TB,N,V_secureVariantEnabled) secureVariantEnabled;
@property (TB,N,GisRecording,V_recording) recording;
@property (Tq,N,V_secureVariantType) secureVariantType;
```

## Class methods

```
+[LAUIPearlGlyphStaticConfiguration createDefaultConfiguration];
+[LAUIPearlGlyphStaticConfiguration createSystemApertureConfiguration];
```

## Instance methods

```
-[LAUIPearlGlyphStaticConfiguration isRecording];
-[LAUIPearlGlyphStaticConfiguration init];
-[LAUIPearlGlyphStaticConfiguration setRecording:];
-[LAUIPearlGlyphStaticConfiguration setInitialStyle:];
-[LAUIPearlGlyphStaticConfiguration setSecureVariantEnabled:];
-[LAUIPearlGlyphStaticConfiguration setSecureVariantType:];
-[LAUIPearlGlyphStaticConfiguration setLineThicknessScale:];
-[LAUIPearlGlyphStaticConfiguration checkmarkThicknessScale];
-[LAUIPearlGlyphStaticConfiguration initialStyle];
-[LAUIPearlGlyphStaticConfiguration lineThicknessScale];
-[LAUIPearlGlyphStaticConfiguration pathStyle];
-[LAUIPearlGlyphStaticConfiguration secureVariantEnabled];
-[LAUIPearlGlyphStaticConfiguration secureVariantType];
-[LAUIPearlGlyphStaticConfiguration setCheckmarkThicknessScale:];
-[LAUIPearlGlyphStaticConfiguration setPathStyle:];
```
