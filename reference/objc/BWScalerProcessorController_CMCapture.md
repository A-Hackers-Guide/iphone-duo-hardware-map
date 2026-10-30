# `BWScalerProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWScalerProcessorControllerInputUpdatesDelegate`
- 2 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _pixelTransferSessionByMediaKey;
@"NSMutableDictionary" _formatDescriptionByMediaKey;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWScalerProcessorController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWScalerProcessorController process];
-[BWScalerProcessorController dealloc];
-[BWScalerProcessorController reset];
-[BWScalerProcessorController initWithConfiguration:];
-[BWScalerProcessorController prepare];
-[BWScalerProcessorController requestForInput:delegate:errOut:];
-[BWScalerProcessorController inputChanged:];
```
