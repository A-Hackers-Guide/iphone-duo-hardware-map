# `TUCollaborationHighlightProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SWHighlightCenterDelegate`, `TUCollaborationProvider`
- 4 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<TUCollaborationProviderDelegate>" delegate;
@"SWHighlightCenter" _highlightCenter;
@"NSMutableDictionary" _collaborationIdentifierToPendingCollaborations;
@"NSMutableDictionary" _collaborationIdentifierToBundleIDs;
```

## Properties

```
@property (T@"SWHighlightCenter",R,N,V_highlightCenter) highlightCenter;
@property (T@"NSMutableDictionary",R,N,V_collaborationIdentifierToPendingCollaborations) collaborationIdentifierToPendingCollaborations;
@property (T@"NSMutableDictionary",R,N,V_collaborationIdentifierToBundleIDs) collaborationIdentifierToBundleIDs;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<TUCollaborationProviderDelegate>",W,N,Vdelegate) delegate;
```

## Instance methods

```
-[TUCollaborationHighlightProvider init];
-[TUCollaborationHighlightProvider setDelegate:];
-[TUCollaborationHighlightProvider ckBundleIDForCollaborationIdentifier:];
-[TUCollaborationHighlightProvider delegate];
-[TUCollaborationHighlightProvider highlightCenter];
-[TUCollaborationHighlightProvider addTemporaryCollaboration:];
-[TUCollaborationHighlightProvider collaborationHighlightForIdentifier:];
-[TUCollaborationHighlightProvider collaborationIdentifierToBundleIDs];
-[TUCollaborationHighlightProvider collaborationIdentifierToPendingCollaborations];
-[TUCollaborationHighlightProvider highlightCenterHighlightsDidChange:];
```
