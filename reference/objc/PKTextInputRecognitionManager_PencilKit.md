# `PKTextInputRecognitionManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHQueryDelegate`, `CHRecognitionSessionDataSource`, `CHTextInputQueryTargetDataSource`, `PKTextInputDebugStateReporting`
- 7 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _preferOutOfProcessRecognition;
@"NSArray" _recognitionLocales;
@"<PKTextInputRecognitionManagerDataSource>" _currentDataSource;
@"CHRecognitionSession" __recognitionSession;
@"CHTextInputQuery" __textInputQuery;
d __beganRecognitionTimestamp;
d __lastRecognitionDuration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",R,C,N) textInputTargets;
```

## Instance methods

```
-[PKTextInputRecognitionManager dealloc];
-[PKTextInputRecognitionManager fetchContentInfoForTextInputTarget:strokeIdentifiers:completion:];
-[PKTextInputRecognitionManager queryDidUpdateResult:];
-[PKTextInputRecognitionManager strokeProviderSnapshot];
-[PKTextInputRecognitionManager textInputTargetForItemStableIdentifier:strokeIdentifiers:];
-[PKTextInputRecognitionManager textInputTargetForItemStableIdentifier:strokeIdentifiers:simultaneousItemStableIdentifiers:];
-[PKTextInputRecognitionManager textInputTargets];
-[PKTextInputRecognitionManager reportDebugStateDescription:];
```
