# `CAMetalLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 2 instance variables, 31 properties, 73 instance methods, 2 class methods

## Instance variables

```
^v _priv;
@"CADisplay" _cachedDisplay;
```

## Properties

```
@property (TB,N) fenceEnabled;
@property (TB,N) serverSyncEnabled;
@property (TB,N) disableFIFO;
@property (TB,N) lowLatency;
@property (TB,N) allowsDisplayCompositingWithCopy;
@property (TB,N) exclusiveMode;
@property (Td,N) inputTime;
@property (TB,N) nonDefaultColorspace;
@property (Td,N) drawableTimeoutSeconds;
@property (TQ,N) protectionOptions;
@property (TQ,N) textureUsage;
@property (TB,N) premultiplied;
@property (TQ,R,N) displayCompositingInternalStatus;
@property (TB,N) lowWorkload;
@property (T@"CAEDRMetadata",&) EDRMetadata;
@property (TB,N) wantsIOSurfaceCompression;
@property (T@"CADisplay",&,N,V_cachedDisplay) cachedDisplay;
@property (T@"<MTLDevice>",&) device;
@property (T@"<MTLDevice>",R) preferredDevice;
@property (TQ) pixelFormat;
@property (TB) framebufferOnly;
@property (T{CGSize=dd}) drawableSize;
@property (TQ) maximumDrawableCount;
@property (TB) presentsWithTransaction;
@property (T^{CGColorSpace=}) colorspace;
@property (TB,D) wantsExtendedDynamicRangeContent;
@property (T@"CAEDRMetadata",&) EDRMetadata;
@property (TB) displaySyncEnabled;
@property (TB) allowsNextDrawableTimeout;
@property (T@"NSDictionary",C) developerHUDProperties;
@property (T@"<MTLResidencySet>",R) residencySet;
```

## Class methods

```
+[CAMetalLayer defaultValueForKey:];
+[CAMetalLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CAMetalLayer setProtectionOptions:];
-[CAMetalLayer isDrawableAvailable];
-[CAMetalLayer didChangeValueForKey:];
-[CAMetalLayer setContents:];
-[CAMetalLayer setDevice:];
-[CAMetalLayer setColorspace:];
-[CAMetalLayer protectionOptions];
-[CAMetalLayer device];
-[CAMetalLayer init];
-[CAMetalLayer dealloc];
-[CAMetalLayer setLowLatency:];
-[CAMetalLayer lowLatency];
-[CAMetalLayer colorspace];
-[CAMetalLayer layerDidBecomeVisible:];
-[CAMetalLayer shouldArchiveValueForKey:];
-[CAMetalLayer setPremultiplied:];
-[CAMetalLayer discardContents];
-[CAMetalLayer setName:];
-[CAMetalLayer textureUsage];
-[CAMetalLayer pixelFormat];
-[CAMetalLayer setPixelFormat:];
-[CAMetalLayer framebufferOnly];
-[CAMetalLayer setFramebufferOnly:];
-[CAMetalLayer setTextureUsage:];
-[CAMetalLayer premultiplied];
-[CAMetalLayer EDRMetadata];
-[CAMetalLayer setDisableFIFO:];
-[CAMetalLayer setEDRMetadata:];
-[CAMetalLayer preferredDevice];
-[CAMetalLayer setLowWorkload:];
-[CAMetalLayer _defersDidBecomeVisiblePostCommit];
-[CAMetalLayer _didCommitLayer:];
-[CAMetalLayer _display];
-[CAMetalLayer allowsDisplayCompositingWithCopy];
-[CAMetalLayer allowsNextDrawableTimeout];
-[CAMetalLayer cachedDisplay];
-[CAMetalLayer currentDisplay];
-[CAMetalLayer developerHUDProperties];
-[CAMetalLayer disableFIFO];
-[CAMetalLayer displayCompositingInternalStatus];
-[CAMetalLayer displaySyncEnabled];
-[CAMetalLayer drawableSize];
-[CAMetalLayer drawableTimeoutSeconds];
-[CAMetalLayer exclusiveMode];
-[CAMetalLayer fenceEnabled];
-[CAMetalLayer inputTime];
-[CAMetalLayer lowWorkload];
-[CAMetalLayer maximumDrawableCount];
-[CAMetalLayer newDrawable];
-[CAMetalLayer nextDrawable];
-[CAMetalLayer nonDefaultColorspace];
-[CAMetalLayer presentsWithTransaction];
-[CAMetalLayer removeBackBuffers];
-[CAMetalLayer residencySet];
-[CAMetalLayer serverSyncEnabled];
-[CAMetalLayer setAllowsDisplayCompositingWithCopy:];
-[CAMetalLayer setAllowsNextDrawableTimeout:];
-[CAMetalLayer setCachedDisplay:];
-[CAMetalLayer setColorspace:nonDefault:];
-[CAMetalLayer setDeveloperHUDProperties:];
-[CAMetalLayer setDisplaySyncEnabled:];
-[CAMetalLayer setDrawableSize:];
-[CAMetalLayer setDrawableTimeoutSeconds:];
-[CAMetalLayer setExclusiveMode:];
-[CAMetalLayer setFenceEnabled:];
-[CAMetalLayer setInputTime:];
-[CAMetalLayer setMaximumDrawableCount:];
-[CAMetalLayer setNonDefaultColorspace:];
-[CAMetalLayer setPresentsWithTransaction:];
-[CAMetalLayer setServerSyncEnabled:];
-[CAMetalLayer setWantsIOSurfaceCompression:];
-[CAMetalLayer shimDrawable:];
-[CAMetalLayer wantsIOSurfaceCompression];
```
