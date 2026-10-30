# `WFNetworkRowConfig`

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 21 instance methods, 3 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _network;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _subtitle;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _connectionState;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _problematicConnection;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 _signalBars;
Q context;
B hideConnectionState;
B showInfoButton;
B isEditable;
? infoButtonHandler;
```

## Properties

```
@property (T@"<WFNetworkListRecord>",N,&) network;
@property (T@"NSString",N,C) subtitle;
@property (Tq,N) connectionState;
@property (TB,N) problematicConnection;
@property (TQ,N) signalBars;
@property (TQ,N,Vcontext) context;
@property (TB,N,VhideConnectionState) hideConnectionState;
@property (TB,N,VshowInfoButton) showInfoButton;
@property (TB,N,VisEditable) isEditable;
@property (T@?,N,C) infoButtonHandler;
```

## Class methods

```
+[WFNetworkRowConfig knownNetworkRowConfig];
+[WFNetworkRowConfig settingsNetworkRowConfig];
+[WFNetworkRowConfig setupNetworkRowConfig];
```

## Instance methods

```
-[WFNetworkRowConfig signalBars];
-[WFNetworkRowConfig isEditable];
-[WFNetworkRowConfig connectionState];
-[WFNetworkRowConfig subtitle];
-[WFNetworkRowConfig network];
-[WFNetworkRowConfig init];
-[WFNetworkRowConfig setConnectionState:];
-[WFNetworkRowConfig setIsEditable:];
-[WFNetworkRowConfig setSubtitle:];
-[WFNetworkRowConfig setContext:];
-[WFNetworkRowConfig setSignalBars:];
-[WFNetworkRowConfig context];
-[WFNetworkRowConfig setShowInfoButton:];
-[WFNetworkRowConfig showInfoButton];
-[WFNetworkRowConfig setNetwork:];
-[WFNetworkRowConfig hideConnectionState];
-[WFNetworkRowConfig infoButtonHandler];
-[WFNetworkRowConfig problematicConnection];
-[WFNetworkRowConfig setHideConnectionState:];
-[WFNetworkRowConfig setInfoButtonHandler:];
-[WFNetworkRowConfig setProblematicConnection:];
```
