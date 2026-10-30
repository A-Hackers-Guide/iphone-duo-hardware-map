# `JFXCompositionPlayerRequest`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSString" _uniqueID;
@? _block;
d _queuedTime;
d _startTime;
Q _type;
@? _completionBlock;
@"JFXCompositionPlayer" _player;
Q _signPostID;
```

## Properties

```
@property (T@"NSString",R,N,V_uniqueID) uniqueID;
@property (T@?,C,N,V_block) block;
@property (Td,N,V_queuedTime) queuedTime;
@property (Td,N,V_startTime) startTime;
@property (TQ,N,V_type) type;
@property (T@?,C,N,V_completionBlock) completionBlock;
@property (T@"JFXCompositionPlayer",W,V_player) player;
@property (TQ,R,N,V_signPostID) signPostID;
```

## Class methods

```
+[JFXCompositionPlayerRequest stringFromRequestType:];
```

## Instance methods

```
-[JFXCompositionPlayerRequest player];
-[JFXCompositionPlayerRequest block];
-[JFXCompositionPlayerRequest setCompletionBlock:];
-[JFXCompositionPlayerRequest completionBlock];
-[JFXCompositionPlayerRequest setBlock:];
-[JFXCompositionPlayerRequest startTime];
-[JFXCompositionPlayerRequest setPlayer:];
-[JFXCompositionPlayerRequest uniqueID];
-[JFXCompositionPlayerRequest setType:];
-[JFXCompositionPlayerRequest type];
-[JFXCompositionPlayerRequest setStartTime:];
-[JFXCompositionPlayerRequest description];
-[JFXCompositionPlayerRequest didCancel];
-[JFXCompositionPlayerRequest didBegin];
-[JFXCompositionPlayerRequest queuedTime];
-[JFXCompositionPlayerRequest setQueuedTime:];
-[JFXCompositionPlayerRequest didComplete];
-[JFXCompositionPlayerRequest didEnqueue];
-[JFXCompositionPlayerRequest initWithBlock:ofType:];
-[JFXCompositionPlayerRequest signPostID];
```
