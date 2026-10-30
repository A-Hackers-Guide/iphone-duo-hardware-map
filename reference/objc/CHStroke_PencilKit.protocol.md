# `CHStroke` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"<CHStrokeIdentifier>",R,N) strokeIdentifier;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (TQ,R,N) strokeAttributes;
@property (Td,R,N) startTimestamp;
@property (Td,R,N) endTimestamp;
@property (TB,R,N) isFinished;
```

## Instance methods

```
-[CHStroke isFinished];
-[CHStroke startTimestamp];
-[CHStroke bounds];
-[CHStroke endTimestamp];
-[CHStroke encodedStrokeIdentifier];
-[CHStroke enumeratePointsWithDistanceStep:usingBlock:];
-[CHStroke enumeratePointsWithTimestep:usingBlock:];
-[CHStroke strokeAttributes];
-[CHStroke strokeIdentifier];
```
