# `NSNetService`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 8 properties, 31 instance methods, 2 class methods

## Instance variables

```
@ _netService;
@ _delegate;
@ _reserved;
```

## Properties

```
@property (T@"<NSNetServiceDelegate>") delegate;
@property (TB) includesPeerToPeer;
@property (T@"NSString",R,C) name;
@property (T@"NSString",R,C) type;
@property (T@"NSString",R,C) domain;
@property (T@"NSString",R,C) hostName;
@property (T@"NSArray",R,C) addresses;
@property (Tq,R) port;
```

## Class methods

```
+[NSNetService dataFromTXTRecordDictionary:];
+[NSNetService dictionaryFromTXTRecordData:];
```

## Instance methods

```
-[NSNetService startMonitoring];
-[NSNetService publish];
-[NSNetService domain];
-[NSNetService init];
-[NSNetService hostName];
-[NSNetService stop];
-[NSNetService dealloc];
-[NSNetService addresses];
-[NSNetService stopMonitoring];
-[NSNetService removeFromRunLoop:forMode:];
-[NSNetService setDelegate:];
-[NSNetService port];
-[NSNetService type];
-[NSNetService delegate];
-[NSNetService scheduleInRunLoop:forMode:];
-[NSNetService hash];
-[NSNetService description];
-[NSNetService isEqual:];
-[NSNetService name];
-[NSNetService resolve];
-[NSNetService TXTRecordData];
-[NSNetService _setIncludesAWDL:];
-[NSNetService getInputStream:outputStream:];
-[NSNetService includesPeerToPeer];
-[NSNetService initWithCFNetService:];
-[NSNetService initWithDomain:type:name:];
-[NSNetService initWithDomain:type:name:port:];
-[NSNetService publishWithOptions:];
-[NSNetService resolveWithTimeout:];
-[NSNetService setIncludesPeerToPeer:];
-[NSNetService setTXTRecordData:];
```
