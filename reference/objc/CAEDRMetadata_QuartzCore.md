# `CAEDRMetadata`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 0 properties, 12 instance methods, 8 class methods

## Instance variables

```
^{_CAEDRMetadataPrivate={?=SSSSSSSSII}{?=SS}@@Bf} _priv;
```

## Class methods

```
+[CAEDRMetadata supportsSecureCoding];
+[CAEDRMetadata isAvailable];
+[CAEDRMetadata HDR10MetadataWithMinLuminance:maxLuminance:opticalOutputScale:];
+[CAEDRMetadata HLGMetadata];
+[CAEDRMetadata HDR10MetadataWithDisplayInfo:contentInfo:opticalOutputScale:];
+[CAEDRMetadata HDR10PlusMetadataWithDisplayInfo:contentInfo:plusMetadata:opticalOutputScale:];
+[CAEDRMetadata HLGMetadataWithAmbientViewingEnvironment:];
+[CAEDRMetadata setMetadata:onSurface:];
```

## Instance methods

```
-[CAEDRMetadata dealloc];
-[CAEDRMetadata encodeWithCoder:];
-[CAEDRMetadata description];
-[CAEDRMetadata initWithCoder:];
-[CAEDRMetadata copyWithZone:];
-[CAEDRMetadata isEqual:];
-[CAEDRMetadata initWithBT2100HLG];
-[CAEDRMetadata initWithMasteringDisplayMinNits:maxNits:opticalOutputScale:];
-[CAEDRMetadata initWithSEIAmbientViewingEnvironment:];
-[CAEDRMetadata initWithSEIMasteringDisplayData:contentLightLevelData:];
-[CAEDRMetadata initWithSEIMasteringDisplayData:contentLightLevelData:opticalOutputScale:];
-[CAEDRMetadata initWithSEIMasteringDisplayData:contentLightLevelData:plusMetadata:opticalOutputScale:];
```
