drop table if exists s_69cd1f4046f393adf2a7697f8ae5a8f9.all_records;
create table s_69cd1f4046f393adf2a7697f8ae5a8f9.all_records as (
    select
        vendor_id
        , org_id
        , shift_id
        , first_name
        , middle_name
        , last_name
        , name_suffix
        , voting_street_address_one
        , voting_street_address_two
        , voting_city
        , voting_state
        , voting_zipcode
        , mailing_street_address_one
        , mailing_street_address_two
        , mailing_city
        , mailing_state
        , mailing_zipcode
        , county
        , gender
        , date_of_birth
        , phone_number
        , email_address
        , updated_at
        , party
        , name_prefix
        , ethnicity
        , latitude
        , longitude
        , completed
        , registration_date
        , shift_type
        , locations_state
        , program_type
        , program_sub_type
        , collection_medium
        , office
        , field_start
        , field_end
        , evc_month
        , evc_year
    from public.vendor_x_registrations_deduped

)
;
