# `BWJasperColorStillsExecutorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWJasperColorStillsExecutorInputDelegate`
- 9 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"FigStateMachine" _stateMachine;
@"BWJasperColorStillsExecutorControllerConfiguration" _configuration;
@"ADJasperColorStillsExecutor" _adStillImageExecutor;
Q _engineType;
@"NSMutableArray" _requestQueue;
@"BWJasperColorStillsExecutorRequest" _currentRequest;
^{opaqueCMFormatDescription=} _depthFormatDescription;
{?="columns"[4]} _identityMatrix;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _inputROI;
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
+[BWJasperColorStillsExecutorController initialize];
```

## Instance methods

```
-[BWJasperColorStillsExecutorController purgeResources];
-[BWJasperColorStillsExecutorController finishProcessingCurrentInputNow];
-[BWJasperColorStillsExecutorController dealloc];
-[BWJasperColorStillsExecutorController initWithConfiguration:];
-[BWJasperColorStillsExecutorController type];
-[BWJasperColorStillsExecutorController cancelProcessing];
-[BWJasperColorStillsExecutorController enqueueInputForProcessing:delegate:];
-[BWJasperColorStillsExecutorController inputReadyToExecute:];
```
