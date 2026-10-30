# `CMInferenceUtils`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _networksV1;
@"NSArray" _networksV2;
@"NSArray" _developNetworksV1;
@"NSArray" _developNetworksV2;
@"NSRegularExpression" _platformRegExpPatternV1;
@"NSRegularExpression" _platformRegExpPatternV2;
@"NSString" _imagingNetworksPath;
@"NSString" _developNetworksPath;
```

## Class methods

```
+[CMInferenceUtils sharedInstance];
+[CMInferenceUtils aneCount];
```

## Instance methods

```
-[CMInferenceUtils init];
-[CMInferenceUtils _getNetworkPath:isE5:fsNetworks:searchPath:];
-[CMInferenceUtils availableImagingNetworksWithExtension:atPath:];
-[CMInferenceUtils getNetworkPath:isE5:];
```
