# `ADM_Mock_Factory`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HAL_DSP_Factory`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
i _featureFlag;
@"MockPropertySet" _libraryProperties;
```

## Properties

```
@property (Ti,N,V_featureFlag) featureFlag;
@property (T@"MockPropertySet",&,N,V_libraryProperties) libraryProperties;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ADM_Mock_Factory init];
-[ADM_Mock_Factory dealloc];
-[ADM_Mock_Factory featureFlag];
-[ADM_Mock_Factory setFeatureFlag:];
-[ADM_Mock_Factory createProcessor:withHost:];
-[ADM_Mock_Factory getFactoryPropertySet];
-[ADM_Mock_Factory libraryProperties];
-[ADM_Mock_Factory setLibraryProperties:];
```
