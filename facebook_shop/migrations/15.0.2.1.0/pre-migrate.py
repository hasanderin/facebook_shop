def migrate(cr, version):
    cr.execute(
        "UPDATE product_data_feed_column "
        "SET special_type='product_attribute_multi' "
        "WHERE special_type='product_attribute'")
