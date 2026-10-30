# `NWStreamPair`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__CFNCoreLoggable`
- 15 instance variables, 0 properties, 1 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_nw_connection>" _connection;
^v _rs;
^v _ws;
@"NSObject<OS_dispatch_queue>" _queue;
C _doneInitialRead;
^{__CFError=} _readError;
^{__CFError=} _writeError;
^{ReadBuffer=^^?q@qC} _readData;
C _atEOF;
C _wsClosing;
C _rsClosing;
^{__CFData=} _cachedPeerName;
^{__SecTrust=} _cachedTrust;
^{__CFArray=} _cachedPeerCerts;
q _outstandingWrites;
```

## Instance methods

```
-[NWStreamPair dealloc];
```
