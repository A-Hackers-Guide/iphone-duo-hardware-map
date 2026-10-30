# `PKReplicaEntry`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`
- 5 instance variables, 5 properties, 14 instance methods, 0 class methods

## Instance variables

```
I _replicaUUIDIndex;
I _clock;
I _subclock;
B _inUse;
@"PKDrawingConcrete" _drawing;
```

## Properties

```
@property (TI,N,V_replicaUUIDIndex) replicaUUIDIndex;
@property (TI,N,V_clock) clock;
@property (TI,N,V_subclock) subclock;
@property (TB,N,V_inUse) inUse;
@property (T@"PKDrawingConcrete",N,V_drawing) drawing;
```

## Instance methods

```
-[PKReplicaEntry drawing];
-[PKReplicaEntry clock];
-[PKReplicaEntry setClock:];
-[PKReplicaEntry setInUse:];
-[PKReplicaEntry setDrawing:];
-[PKReplicaEntry encodeWithCoder:];
-[PKReplicaEntry description];
-[PKReplicaEntry initWithCoder:];
-[PKReplicaEntry inUse];
-[PKReplicaEntry replicaUUIDIndex];
-[PKReplicaEntry setReplicaUUIDIndex:];
-[PKReplicaEntry setSubclock:];
-[PKReplicaEntry subclock];
-[PKReplicaEntry initWithReplicaUUIDIndex:clock:subclock:inUse:forDrawing:];
```
