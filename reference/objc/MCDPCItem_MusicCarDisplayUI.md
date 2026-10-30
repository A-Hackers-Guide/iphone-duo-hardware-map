# `MCDPCItem`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _isPlayable;
B _isContainer;
B _isCloudItem;
B _currentlyPlaying;
B _isExplicitItem;
f _playbackProgress;
@"NSString" _identifier;
@"NSString" _title;
@"NSString" _subtitle;
@"NSData" _artworkData;
@"UIImage" _artworkImage;
@"MCDPCModel" _model;
```

## Properties

```
@property (T@"MCDPCModel",R,W,N,V_model) model;
@property (TB,N,V_currentlyPlaying) currentlyPlaying;
@property (T@"UIImage",&,N,V_artworkImage) artworkImage;
@property (T@"NSString",R,N,V_identifier) identifier;
@property (T@"NSString",R,N,V_title) title;
@property (T@"NSString",R,N,V_subtitle) subtitle;
@property (T@"NSData",R,N,V_artworkData) artworkData;
@property (Tf,R,N,V_playbackProgress) playbackProgress;
@property (TB,R,N,V_isPlayable) isPlayable;
@property (TB,R,N,V_isContainer) isContainer;
@property (TB,R,N,V_isCloudItem) isCloudItem;
@property (TB,R,N,V_isExplicitItem) isExplicitItem;
```

## Instance methods

```
-[MCDPCItem isPlayable];
-[MCDPCItem model];
-[MCDPCItem subtitle];
-[MCDPCItem artworkData];
-[MCDPCItem identifier];
-[MCDPCItem playbackProgress];
-[MCDPCItem isContainer];
-[MCDPCItem title];
-[MCDPCItem description];
-[MCDPCItem setCurrentlyPlaying:];
-[MCDPCItem artworkImage];
-[MCDPCItem setArtworkImage:];
-[MCDPCItem isExplicitItem];
-[MCDPCItem isCloudItem];
-[MCDPCItem currentlyPlaying];
-[MCDPCItem _initWithModel:MRContentItem:];
```
