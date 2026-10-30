# `SecSessionInfo`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
I _ticket_age_add;
@"NSData" _psk;
@"NSData" _psk_id;
Q _ticket_creation_time;
Q _ticket_lifetime;
```

## Properties

```
@property (T@"NSData",&,V_psk) psk;
@property (T@"NSData",&,V_psk_id) psk_id;
@property (TI,V_ticket_age_add) ticket_age_add;
@property (TQ,V_ticket_creation_time) ticket_creation_time;
@property (TQ,V_ticket_lifetime) ticket_lifetime;
```

## Instance methods

```
-[SecSessionInfo setTicket_age_add:];
-[SecSessionInfo ticket_lifetime];
-[SecSessionInfo psk];
-[SecSessionInfo ticket_creation_time];
-[SecSessionInfo setPsk:];
-[SecSessionInfo setTicket_creation_time:];
-[SecSessionInfo psk_id];
-[SecSessionInfo initWithPSK:::::];
-[SecSessionInfo setPsk_id:];
-[SecSessionInfo ticket_age_add];
-[SecSessionInfo setTicket_lifetime:];
```
