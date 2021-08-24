# JPA Cascade

## Cascade란?
부모 엔티티의 영속성 상태 변화를 자식 엔티티에게 전파시키는 옵션.
`@ManyToOne`, `@OneToMany`, `@OneToOne` 등의 연관관계 어노테이션에 옵션으로 줄 수 있다.

## CascadeType
CascadeType은 모두 EntityManager의 메서드에 대응한다.
ex) PERSIST: `em.persist()`시 자식 엔티티도 `persist()`됨
- ALL (아래의 모든 옵션이 포함됨)
- PERSIST
- MERGE
- REMOVE
- REFRESH
- DETACH

## 주의점
이미 영속화된 부모엔티티에 비영속상태의 자식엔티티를 연결시켜도 자식은 영속상태가 되지 않는다.
영속성 상태가 변화될 때 이미 연결된 자식엔티티도 같이 변화시키는 것일 뿐이다.
