# `PKVisualizationManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CHVisualizationManagerDelegate`
- 2 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"<PKVisualizationManager>" _delegate;
@"CHVisualizationManager" _chVisualizationManager;
```

## Properties

```
@property (T@"CHVisualizationManager",&,N,V_chVisualizationManager) chVisualizationManager;
@property (TB,N) recognitionStatusReportingEnabled;
@property (T@"<PKVisualizationManager>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PKVisualizationManager availableRecognitionStatusKeys];
+[PKVisualizationManager localizedNameForRecognitionStatusKey:];
```

## Instance methods

```
-[PKVisualizationManager dealloc];
-[PKVisualizationManager setDelegate:];
-[PKVisualizationManager delegate];
-[PKVisualizationManager initWithRecognitionSession:];
-[PKVisualizationManager valueForRecognitionStatusKey:];
-[PKVisualizationManager visualizationManager:needsDisplayInRect:];
-[PKVisualizationManager visualizationManagerDidUpdateSessionStatus:];
-[PKVisualizationManager visualizationManagerNeedsDisplay:];
-[PKVisualizationManager chVisualizationManager];
-[PKVisualizationManager recognitionStatusReportingEnabled];
-[PKVisualizationManager setChVisualizationManager:];
-[PKVisualizationManager setRecognitionStatusReportingEnabled:];
```
