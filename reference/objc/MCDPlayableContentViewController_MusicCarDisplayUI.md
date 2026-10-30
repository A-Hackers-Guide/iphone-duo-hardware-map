# `MCDPlayableContentViewController`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- Protocols: `UINavigationControllerDelegate`
- 8 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"MCDPCModel" _model;
@"MCDPCContainer" _rootContainer;
@"NSArray" _stackToRebuild;
B _hasBrowsableContent;
B _hasSectionedContent;
B _hasLoaded;
@"NSString" _bundleID;
@"NSOperationQueue" _modelInvalidationQueue;
```

## Properties

```
@property (T@"NSOperationQueue",&,N,V_modelInvalidationQueue) modelInvalidationQueue;
@property (T@"NSString",R,C,N,V_bundleID) bundleID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MCDPlayableContentViewController setViewControllers:animated:];
-[MCDPlayableContentViewController initWithBundleID:];
-[MCDPlayableContentViewController viewWillDisappear:];
-[MCDPlayableContentViewController viewWillAppear:];
-[MCDPlayableContentViewController bundleID];
-[MCDPlayableContentViewController _setupView];
-[MCDPlayableContentViewController refreshNavigationStackForLaunch];
-[MCDPlayableContentViewController _createRootViewController];
-[MCDPlayableContentViewController _createSectionedRootViewController];
-[MCDPlayableContentViewController _modelDidInvalidate:];
-[MCDPlayableContentViewController _nowPlayingIdentifiersChanged:];
-[MCDPlayableContentViewController _populateStack];
-[MCDPlayableContentViewController currentStack];
-[MCDPlayableContentViewController initWithBundleID:stack:];
-[MCDPlayableContentViewController modelInvalidationQueue];
-[MCDPlayableContentViewController setModelInvalidationQueue:];
```
