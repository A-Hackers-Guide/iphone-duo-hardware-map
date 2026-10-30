# `CLRegulatoryConfig`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CLRegulatoryConfigInternal, std::default_delete<CLRegulatoryConfigInternal>>=""{?="__ptr_"^{CLRegulatoryConfigInternal}}} _config;
```

## Instance methods

```
-[CLRegulatoryConfig fetchInfoForLocation:withReply:];
-[CLRegulatoryConfig addConfigForIsoList:config:error:];
-[CLRegulatoryConfig addConfigForRegionList:config:error:];
-[CLRegulatoryConfig fetchConfigForLocation:withReply:];
-[CLRegulatoryConfig initWithQueue:defaultConfig:];
-[CLRegulatoryConfig setExtendedBorderDetection:withExtendedDistance:];
```
