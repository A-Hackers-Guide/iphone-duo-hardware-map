# `DSP_HAL_Mock_Factory`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_Factory`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
i _featureFlag;
@"DSP_HAL_Mock_PropertySet" _libraryProperties;
```

## Properties

```
@property (Ti,N,V_featureFlag) featureFlag;
@property (T@"DSP_HAL_Mock_PropertySet",&,N,V_libraryProperties) libraryProperties;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSP_HAL_Mock_Factory init];
-[DSP_HAL_Mock_Factory dealloc];
-[DSP_HAL_Mock_Factory featureFlag];
-[DSP_HAL_Mock_Factory setFeatureFlag:];
-[DSP_HAL_Mock_Factory createProcessor:withHost:];
-[DSP_HAL_Mock_Factory getFactoryPropertySet];
-[DSP_HAL_Mock_Factory libraryProperties];
-[DSP_HAL_Mock_Factory setLibraryProperties:];
```
