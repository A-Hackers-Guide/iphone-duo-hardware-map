# `_TtC7Network22NetworkActorFileHandle`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_TtCs12_SwiftObject`
- 10 instance variables, 0 properties, 0 instance methods, 0 class methods

## Instance variables

```
_$sSS filename;
Swift.Int64 fileSize;
Foundation.UUID handleID;
Network.NetworkFileTransferCoordinator ? _transferCoordinator;
Foundation.URL sourceURL;
os.OSAllocatedUnfairLock _$syt lock;
_$sSa -> Swift.AsyncThrowingStream.Continuation Network.NetworkActorFileHandle.TransferProgress Swift.Error _$s_G -> progressContinuations;
Swift.Result _$syyt Swift.Error ? result;
Swift.Bool userCancelled;
Swift.Bool isRemote;
```
