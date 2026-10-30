# `SBSystemNotesContentPresentationContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBSSystemNotesPresentationConfiguration" _requestedConfiguration;
Q _source;
@"SBSystemNotesPositionConfiguration" _positionConfiguration;
```

## Properties

```
@property (T@"SBSSystemNotesPresentationConfiguration",&,N,V_requestedConfiguration) requestedConfiguration;
@property (TQ,N,V_source) source;
@property (T@"SBSystemNotesPositionConfiguration",&,N,V_positionConfiguration) positionConfiguration;
```

## Instance methods

```
-[SBSystemNotesContentPresentationContext setSource:];
-[SBSystemNotesContentPresentationContext source];
-[SBSystemNotesContentPresentationContext requestedConfiguration];
-[SBSystemNotesContentPresentationContext initWithLaunchBundleID:presentationMode:source:positionConfiguration:];
-[SBSystemNotesContentPresentationContext initWithRequestedConfiguration:source:positionConfiguration:];
-[SBSystemNotesContentPresentationContext positionConfiguration];
-[SBSystemNotesContentPresentationContext setPositionConfiguration:];
-[SBSystemNotesContentPresentationContext setRequestedConfiguration:];
```
